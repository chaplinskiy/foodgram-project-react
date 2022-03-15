from drf_extra_fields.fields import Base64ImageField

from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer, UserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from recipes.models import (Ingredient, Recipe, RecipeUser, RecipeUserCart,
                            RecipeIngredientAmount, Tag)
from users.models import Subscription

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Ingredient


class RecipeIngredientAmountSerializer(serializers.HyperlinkedModelSerializer):
    amount = serializers.IntegerField(min_value=1)
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit'
    )

    class Meta:
        fields = [
            'id',
            'name',
            'measurement_unit',
            'amount'
        ]
        model = RecipeIngredientAmount


class AddIngredientSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField(min_value=1)
    id = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())

    class Meta:
        fields = [
            'amount',
            'id'
        ]
        model = RecipeIngredientAmount


class RecipeListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    ingredients = RecipeIngredientAmountSerializer(
        source='recipeingredientamount_set',
        many=True,
        required=True
    )
    is_favorited = serializers.SerializerMethodField(read_only=True)
    is_in_shopping_cart = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'author',
            'image',
            'ingredients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'tags',
            'text',
            'cooking_time'
        ]

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return RecipeUser.objects.filter(
            recipe=obj,
            user=request.user
        ).exists()

    def get_is_in_shopping_cart(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return RecipeUserCart.objects.filter(
            recipe=obj,
            user=request.user
        ).exists()


class RecipeCUDSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    ingredients = AddIngredientSerializer(many=True)
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = [
            'image',
            'ingredients',
            'name',
            'tags',
            'text',
            'cooking_time'
        ]

    def validate(self, data):
        ingredients = data['ingredients']
        ingredients_list = []
        for ingredient in ingredients:
            ingredient_id = ingredient['id']
            if ingredient_id in ingredients_list:
                raise serializers.ValidationError({
                    'ingredients': 'Should be unique.'
                })
            ingredients_list.append(ingredient_id)

        tags = data['tags']
        if not tags:
            raise serializers.ValidationError({
                'tags': 'At least one tag required.'
            })
        tags_list = []
        for tag in tags:
            if tag in tags_list:
                raise serializers.ValidationError({
                    'tags': 'Should be unique.'
                })
            tags_list.append(tag)
        return data

    @staticmethod
    def create_ingredients(ingredients, recipe):
        for ingredient in ingredients:
            RecipeIngredientAmount.objects.create(
                recipe=recipe, ingredient=ingredient['id'],
                amount=ingredient['amount']
            )

    @staticmethod
    def create_tags(tags, recipe):
        for tag in tags:
            recipe.tags.add(tag)

    def create(self, validated_data):
        author = self.context.get('request').user
        tags = validated_data.pop('tags')
        ingredients = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(author=author, **validated_data)
        self.create_tags(tags, recipe)
        self.create_ingredients(ingredients, recipe)
        return recipe

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RecipeListSerializer(instance, context=context).data

    def update(self, instance, validated_data):
        instance.tags.clear()
        RecipeIngredientAmount.objects.filter(recipe=instance).all().delete()
        self.create_tags(validated_data.pop('tags'), instance)
        self.create_ingredients(validated_data.pop('ingredients'), instance)
        return super().update(instance, validated_data)


class RecipeMinifiedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            'id',
            'name',
            'image',
            'cooking_time'
        ]


class RecipeUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'recipe',
            'user'
        ]
        model = RecipeUser

    def validate(self, data):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        recipe = data['recipe']
        if RecipeUser.objects.filter(
            user=request.user, recipe=recipe
        ).exists():
            raise serializers.ValidationError({
                'status': 'Already favorited.'
            })
        return data

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RecipeMinifiedSerializer(instance.recipe, context=context).data


class RecipeUserCartSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'recipe',
            'user'
        ]
        model = RecipeUserCart

    def validate(self, data):
        request = self.context.get('request')
        recipe = data['recipe']
        if RecipeUserCart.objects.filter(
            user=request.user, recipe=recipe
        ).exists():
            raise serializers.ValidationError({
                'status': 'This recipe is already in your cart.'
            })
        return data

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return RecipeMinifiedSerializer(instance.recipe, context=context).data


class SubscriptionSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()
    id = serializers.SerializerMethodField(read_only=True)
    username = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()
    is_subscribed = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count'
        ]

    def get_id(self, obj):
        return obj.following.id

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        user = request.user
        return Subscription.objects.filter(
            following=obj.following,
            follower=user
        ).exists()

    def get_recipes(self, obj):
        request = self.context.get('request')
        recipes_limit = request.query_params.get('recipes_limit')
        if recipes_limit is not None:
            queryset = Recipe.objects.filter(
                author=obj.following
            )[:int(recipes_limit)]
        else:
            queryset = Recipe.objects.filter(author=obj.following)
        return RecipeMinifiedSerializer(queryset, many=True).data

    def get_recipes_count(self, obj):
        return Recipe.objects.filter(author=obj.following).count()


class SubscriptionCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            'following',
            'follower'
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Subscription.objects.all(),
                fields=('following', 'follower'),
                message='Subscription exists'
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return SubscriptionSerializer(instance, context=context).data

    def validate(self, data):
        if data['follower'] == data['following']:
            raise serializers.ValidationError('Self-subscription prohibited')
        return data


class CustomUserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed'
        ]

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        user = request.user
        return Subscription.objects.filter(
            following=obj,
            follower=user
        ).exists()


class CustomUserCreateSerializer(UserCreateSerializer):
    pass
