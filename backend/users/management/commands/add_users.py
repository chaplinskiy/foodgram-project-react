from csv import reader

from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Users loader."""
    help = "Load users from csv file."

    def handle(self, *args, **kwargs):
        with open(
                'data/users.csv', 'r', encoding='UTF-8') as users:
            for row in reader(users):
                if len(row) == 5:
                    User.objects.get_or_create(
                        username=row[0],
                        password=User.set_password(self, raw_password=row[1]),
                        email=row[2],
                        first_name=row[3],
                        last_name=row[4]
                    )
