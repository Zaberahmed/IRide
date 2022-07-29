from rest_framework import serializers
from Iride_app import models


class Rider_serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'Name',
            'Age',
            'Weight'
        )
        model = models.Rider
