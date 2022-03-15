from django.contrib import admin

from .models import (Ingredient, Recipe, RecipeIngredientAmount,
                     RecipeTag, RecipeUser, RecipeUserCart, Tag)


class RecipeIngredientAmountInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 0


class RecipeTagInLine(admin.TabularInline):
    model = Recipe.tags.through
    extra = 0


class RecipeUserInLine(admin.TabularInline):
    model = Recipe.is_favorited.through
    extra = 0


class RecipeUserCartInLine(admin.TabularInline):
    model = Recipe.is_in_shopping_cart.through
    extra = 0


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name', 'text')
    list_filter = ('name', 'author', 'tags')
    empty_value_display = '-пусто-'
    inlines = [RecipeIngredientAmountInLine, RecipeTagInLine,
               RecipeUserInLine, RecipeUserCartInLine]


class RecipeIngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('amount', 'ingredient', 'recipe')
    list_filter = ('recipe',)


class RecipeTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'recipe')


class RecipeUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user',)


class RecipeUserCartAdmin(RecipeUserAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredientAmount, RecipeIngredientAmountAdmin)
admin.site.register(RecipeTag, RecipeTagAdmin)
admin.site.register(RecipeUser, RecipeUserAdmin)
admin.site.register(RecipeUserCart, RecipeUserCartAdmin)
admin.site.register(Tag, TagAdmin)
