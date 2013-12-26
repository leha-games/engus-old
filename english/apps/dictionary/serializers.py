from rest_framework import serializers
from .models import Word, Definition


class UrlFileField(serializers.FileField): 
    def to_native(self, value): 
        if value:
            return value.url
        else:
            return None


class DefinitionSerializer(serializers.ModelSerializer):
    part_of_speach = serializers.Field(source='get_part_of_speach_display')
    illustration = UrlFileField('illustration')
    example_illustration = UrlFileField('example_illustration')
    
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
