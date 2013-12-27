from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'word', 'is_learning', 'created', 'last_repeat', 'repeat_level', 'next_repeat', )
