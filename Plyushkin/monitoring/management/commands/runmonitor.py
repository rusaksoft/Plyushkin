from django.core.management.base import BaseCommand, CommandError
# from polls.models import Poll

from datetime import datetime
from monitoring import bacumon
from monitoring import models

class Command(BaseCommand):
    help = 'Starting monitoring. Scheduler will be started which run jobs to check backup actions.'

    def add_arguments(self, parser):
        pass
        # parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        
        self.stdout.write("Start bacumon "+datetime.now().isoformat())

        bacumon.check_all()

        self.stdout.write(self.style.SUCCESS('Successfully run checks'))

        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
