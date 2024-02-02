from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    help = "Creates an admin user if it does not exist"

    def handle(self, *args, **options):
        User = get_user_model()
        admin_username = settings.ADMIN_USERNAME
        admin_email = settings.ADMIN_EMAIL
        admin_password = settings.ADMIN_PASSWORD

        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(
                username=admin_username, email=admin_email, password=admin_password
            )
            self.stdout.write(self.style.SUCCESS("Successfully created new admin user"))
        else:
            self.stdout.write(self.style.SUCCESS("Admin user already exists"))
