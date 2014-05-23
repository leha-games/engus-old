from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    word_short_def = serializers.Field(source='word.short_definition')

    class Meta:
        model = Card
        fields = ('id', 'word', 'word_short_def', 'status', 'when_learned', 'level', 'created', )
        read_only_fields = ('created', )
