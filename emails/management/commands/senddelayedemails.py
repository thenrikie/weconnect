from django.core.management.base import BaseCommand, CommandError
from emails.models import Queue
from emails import sender
from projects.models import Project
from pitches.models import Pitch

import datetime

class Command(BaseCommand):
    help = 'Send Delayed Emails'
    def handle(self, *args, **options):
        self.stdout.write('Starting Reading Queue...')
        items = Queue.objects.filter(
            state="waiting", 
            start_at__lt=datetime.datetime.now(),
            before_at__gt=datetime.datetime.now()
        )

        for item in items:
            self.stdout.write('Processing item ' + str(item.id) + '; action: ' + str(item.action))

            ### Send 3 proposals ready if still not hire anyone
            if item.action == "three_proposals_ready":
                try:
                    project = Project.objects.get(id=item.item_id)
                    if not project.awarded():
                        sender.three_proposals_ready(project.user.email, {
                            'project_type': str(project.sub_business.first()).lower(),
                            'pitch': project.ready_pitch().first(),
                            'name': project.user.first_name
                        })

                except Project.DoesNotExist:
                    pass


            elif item.action == "final_reminder_project":
                try:
                    project = Project.objects.get(id=item.item_id)
                    if not project.awarded():
                        sender.final_reminder_project(project.user.email, {
                            'project_type': str(project.sub_business.first()).lower(),
                            'pitch': project.ready_pitch().first(),
                            'role': project.sub_business.first().role.lower() + 's',
                            'name': project.user.first_name
                        })

                except Project.DoesNotExist:
                    pass

            elif item.action == "cancel_warning_project":
                try:
                    project = Project.objects.get(id=item.item_id)
                    if not project.awarded():
                        sender.cancel_warning_project(project.user.email, {
                            'project_type': str(project.sub_business.first()).lower(),
                            'pitch': project.ready_pitch().first(),
                            'name': project.user.first_name
                        })

                        #enqueue cancel project action
                        q = Queue(
                            item_id=project.id,
                            item_object='project',
                            start_at = datetime.datetime.now() + datetime.timedelta(days=2),
                            before_at = datetime.datetime.now() + datetime.timedelta(days=3),
                            action = 'cancel_project'
                        )

                        q.save()

                except Project.DoesNotExist:
                    pass

            elif item.action == "cancel_project":
                try:
                    project = Project.objects.get(id=item.item_id)

                    if not project.awarded():
                        project.cancelled = True
                        project.save()

                        #update all pitches status
                        pitches = project.ready_pitch()

                        for pitch in pitches:
                            pitch.change_state('rejected')
                            pitch.archived = True
                            pitch.save()
                            sender.project_cancel(pitch.company.email, {
                                'name' : pitch.company.first_name,
                                'customer_name': project.user.first_name,
                                'project_type': project.sub_business.first()
                            })

                except Project.DoesNotExist:
                    pass

            elif item.action == "request_for_service_12hrs":
                try:
                    pitch = Pitch.objects.get(id=item.item_id)
                    if pitch.waiting():
                        sender.request_for_service_12hrs(pitch.company.email, {
                            'name': pitch.company.first_name,
                            'customer_name': pitch.project.user.first_name,
                            'project_type':  pitch.project.sub_business.first().name.lower(),
                            'pitch' : pitch
                        })

                except Pitch.DoesNotExist:
                    pass

            elif item.action == "send_a_message_to_project":
                try:
                    pitch = Pitch.objects.get(id=item.item_id)
                    if pitch.accepted():
                        sender.send_a_message_to_project(pitch.company.email, {
                            'name': pitch.company.first_name,
                            'customer_name': pitch.project.user.first_name,
                            'pitch' : pitch
                        })

                except Pitch.DoesNotExist:
                    pass

            item.state="finished"
            item.finished_at = datetime.datetime.now()
            item.save()

        self.stdout.write('Done')