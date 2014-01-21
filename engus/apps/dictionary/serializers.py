from rest_framework import serializers
from .models import Word, Definition, Example


class UrlFileField(serializers.FileField): 
    def to_native(self, value): 
        if value:
            return value.url
        else:
            return None


class ExampleSerializer(serializers.ModelSerializer):
    illustration_url = UrlFileField('illustration', read_only=True)
    
    class Meta:
        model = Example
        fields = ('definition', 'text', 'russian_translation', 'illustration_url', )


class DefinitionSerializer(serializers.ModelSerializer):
    part_of_speach = serializers.Field(source='get_part_of_speach_display')
    
    class Meta:
        model = Definition
        fields = ('id', 'weight', 'part_of_speach', 'definition', 'russian_definition', )
        

class WordSerializer(serializers.ModelSerializer):
    audio_url = UrlFileField('audio', read_only=True)
    definition_set = DefinitionSerializer(many=True)

    class Meta:
        model = Word
        fields = ('word', 'transcription', 'audio_url', 'mueller_definition', 'definition_set', )
