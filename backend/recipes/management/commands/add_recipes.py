import random

from csv import reader

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from recipes.models import Recipe

User = get_user_model()

NUM_ROWS = 5

users = User.objects.all().order_by('?')


class Command(BaseCommand):
    """Recipes loader."""
    help = "Load recipes from csv file (should be in '/backend/data')."

    def handle(self, *args, **kwargs):
        with open(
                'data/recipes.csv', 'r', encoding='UTF-8') as recipes:
            for row in reader(recipes):
                if len(row) == NUM_ROWS:
                    user = random.choice(users)
                    Recipe.objects.get_or_create(
                        author=user,
                        cooking_time=row[1],
                        name=row[2],
                        text=row[4]
                    )
