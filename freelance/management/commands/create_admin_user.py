from django.core.management.base import BaseCommand
from freelance.models import CustomUser


class Command(BaseCommand):
    help = 'Create admin user if it does not exist'

    def handle(self, *args, **kwargs):
        if not CustomUser.objects.filter(username='admin').exists() and not CustomUser.objects.filter(email='admin').exists():
            CustomUser.objects.create_superuser('admin', 'admin@admin.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Admin user created successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))
