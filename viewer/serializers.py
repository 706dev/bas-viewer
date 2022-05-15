from rest_framework import serializers

from . import models


class contentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.content
        fields = [
            "specific_date",
            "file",
            "title",
            "duration",
        ]
