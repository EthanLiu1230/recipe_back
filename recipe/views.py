from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication

# combine view_sets and mixins to create list_Model_view_set
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Manage tags in the database.
    1. requires auth
    2. list tags
    3. tags are specific for the user that is authenticated
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()

    def get_queryset(self):
        """Filter objects for the current authenticated user only."""
        return self.queryset.filter(user=self.request.user).order_by('-name')
