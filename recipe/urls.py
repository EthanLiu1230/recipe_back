from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# routers are for viewSets
router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('/', include(router.urls))
]
