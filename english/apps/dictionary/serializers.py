from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('word', )
        read_only_fields = ('word', )
