from django.core.management.base import BaseCommand
from hrbot.bot import start_bot
from django.core.management import call_command

class Command(BaseCommand):
    def handle(self, *args, **options):
        start_bot()




