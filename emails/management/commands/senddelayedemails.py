from django.core.management.base import BaseCommand, CommandError
from emails.models import Queue
from emails import sender
from projects.models import Project
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
                        sender.three_proposals_ready({
                            'project_type': project.sub_business.first(),
                            'pitch': project.ready_pitch().first(),
                            'name': project.project.user.first_name
                        })

                except Project.DoesNotExist:
                    pass




            item.state="finished"
            item.finished_at = datetime.datetime.now()
            item.save()

        self.stdout.write('Done')