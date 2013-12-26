from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):
    audio = serializers.SerializerMethodField('get_audio_url')

    class Meta:
        model = Word
        fields = ('word', 'transcription', 'audio', 'mueller_definition', )

    def get_audio_url(self, obj):
        if obj.audio:
            return obj.audio.url
        else:
            return None
