from rest_framework import viewsets, permissions

from . import serializers
from . import models


class contentViewSet(viewsets.ModelViewSet):
    """ViewSet for the content class"""

    queryset = models.content.objects.all()
    serializer_class = serializers.contentSerializer
    permission_classes = [permissions.IsAuthenticated]
