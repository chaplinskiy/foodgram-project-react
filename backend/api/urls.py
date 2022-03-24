from django.urls import include, path

from rest_framework import routers

from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(
    r'users/subscriptions',
    views.SubscriptionViewSet,
    basename='subscriptions'
)
router.register(r'users', views.UserViewSet, basename='users')
router.register(
    r'ingredients', views.IngredientViewSet, basename='ingredients'
)
router.register(r'recipes', views.RecipeViewSet, basename='recipes')
router.register(r'tags', views.TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'users/<int:id>/subscribe/',
        views.SubscriptionCreateDestroyView.as_view(),
        name='subscribe'
    ),
    path('auth/', include('djoser.urls.authtoken')),
]
