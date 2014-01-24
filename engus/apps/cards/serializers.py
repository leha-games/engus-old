from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'word', 'learned', 'when_learned', 'level', 'created', )
        read_only_fields = ('created', )
