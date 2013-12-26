from rest_framework import serializers
from .models import Word, Definition


class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = ('weight', 'part_of_speach', 'definition', 'russian_definition', 'illustration', 'example', 'example_russian_translation', 'example_illustration', )
        

class WordSerializer(serializers.ModelSerializer):
    audio = serializers.SerializerMethodField('get_audio_url')
    definition_set = DefinitionSerializer(many=True)

    class Meta:
        model = Word
        fields = ('word', 'transcription', 'audio', 'mueller_definition', 'definition_set', )

    def get_audio_url(self, obj):
        if obj.audio:
            return obj.audio.url
        else:
            return None
