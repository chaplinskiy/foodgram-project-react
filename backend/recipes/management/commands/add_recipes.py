import random

from csv import reader

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from recipes.models import Recipe

User = get_user_model()

NUM_ROWS = 5

# users = User.objects.order_by('?')[:NUM_ROWS]
users = User.objects.all().order_by('?')


class Command(BaseCommand):
    """Ingredients loader."""
    help = "Load ingredients from csv file."

    def handle(self, *args, **kwargs):
        with open(
                'data/recipes.csv', 'r', encoding='UTF-8') as recipes:
            for row in reader(recipes):
                if len(row) == NUM_ROWS:
                    user = random.choice(users)
                    # user = users[0]
                    Recipe.objects.get_or_create(
                        # author=row[0],
                        author=user,
                        cooking_time=row[1],
                        name=row[2],
                        image=row[3],
                        text=row[4]
                    )
                    # user = users[0 + 1]
