from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="sdeer").exists():
            User.objects.create_superuser("sdeer", "sdeery14@gmail.com", "qLPbb91egdjP")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))