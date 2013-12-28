from rest_framework import serializers
from .models import Word, Definition, Example


class UrlFileField(serializers.FileField): 
    def to_native(self, value): 
        if value:
            return value.url
        else:
            return None


class ExampleSerializer(serializers.ModelSerializer):
    illustration = UrlFileField('illustration')
    
    class Meta:
        model = Example
        fields = ('text', 'russian_translation', 'illustration', )


class DefinitionSerializer(serializers.ModelSerializer):
    part_of_speach = serializers.Field(source='get_part_of_speach_display')
    illustration = UrlFileField('illustration')
    example_set = ExampleSerializer(many=True)
    
    class Meta:
        model = Definition
        fields = ('weight', 'part_of_speach', 'definition', 'russian_definition', 'illustration', 'example_set', )
        

class WordSerializer(serializers.ModelSerializer):
    audio = UrlFileField('audio')
    definition_set = DefinitionSerializer(many=True)

    class Meta:
        model = Word
        fields = ('id', 'word', 'transcription', 'audio', 'mueller_definition', 'definition_set', )
