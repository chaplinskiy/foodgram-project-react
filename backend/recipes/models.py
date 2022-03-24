from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название тега',
        db_index=True
    )
    color = models.CharField(
        max_length=7,
        null=True,
        verbose_name='Цвет'
    )
    slug = models.SlugField(
        max_length=200,
        verbose_name='Slug',
        unique=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.slug


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название ингредиента',
        db_index=True
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единицы измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(999, 'Не более 999'),
            MinValueValidator(1, 'Не менее 1')
        ],
        verbose_name='Время приготовления (в минутах)'
    )
    image = models.ImageField(
        blank=True,
        verbose_name='Картинка',
        upload_to='recipes/images'
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    text = models.TextField(
        verbose_name='Описание'
    )
    tags = models.ManyToManyField(
        Tag, through='RecipeTag', verbose_name='Теги'
    )
    ingredients = models.ManyToManyField(
        Ingredient, through='RecipeIngredientAmount'
    )
    is_favorited = models.ManyToManyField(
        User, through='RecipeUser',
        related_name='favorited'
    )
    is_in_shopping_cart = models.ManyToManyField(
        User, through='RecipeUserCart',
        related_name='recipes_in_shopping_cart'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeAux(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        abstract = True


class RecipeIngredientAmount(RecipeAux):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    amount = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Количество'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('recipe', 'ingredient'),
                name='unique_recipeingredientamount_list'
            )
        ]
        verbose_name = 'Количество/ингредиент'
        verbose_name_plural = 'Количества/ингредиент'

    def __str__(self):
        return f'{self.recipe} {self.ingredient} {self.amount}'


class RecipeTag(RecipeAux):
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE,
        verbose_name='Тег'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('recipe', 'tag'),
                name='unique_recipetag_list'
            )
        ]
        verbose_name = 'Тег/рецепт'
        verbose_name_plural = 'Теги/рецепт'

    def __str__(self):
        return f'{self.recipe} {self.tag}'


class RecipeUser(RecipeAux):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_recipeuser'
            )
        ]
        verbose_name = 'Избранное/рецепт'
        verbose_name_plural = 'Избранные/рецепт'

    def __str__(self):
        return f'{self.recipe} {self.user}'


class RecipeUserCart(RecipeAux):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_recipeusercart'
            )
        ]
        ordering = ['-id']
        verbose_name = 'Список покупок/рецепт'
        verbose_name_plural = 'Списки покупок/рецепт'
