from django.core.management.base import BaseCommand, CommandError
from emails.models import Queue
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
            item.state="finished"
            item.finished_at = datetime.datetime.now()
            item.save()

        self.stdout.write('Done')