from rest_framework.authentication import TokenAuthentication

# combine view_sets and mixins to create list_Model_view_set
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from core import models
from recipe import serializers


class BaseRecipeAttrViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        """Return objects for the current authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new object."""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """
    Manage tags in the database.
    1. requires auth
    2. list tags
    3. tags are specific for the user that is authenticated
    """
    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects.all()


class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database."""
    serializer_class = serializers.IngredientSerializer
    queryset = models.Ingredient.objects.all()
