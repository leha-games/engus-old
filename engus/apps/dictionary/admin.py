from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Word, Definition, Example


class ExampleInline(admin.StackedInline):
    model = Example
    extra = 5
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
    }
    

class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'word', 'part_of_speach', 'definition', 'weight', )
    search_fields = ['word__word', ]
    inlines = [
        ExampleInline,
    ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
    }
    list_filter = ('part_of_speach', )
    readonly_fields = ('word', )


class DefinitionInline(admin.StackedInline):
    model = Definition
    extra = 0
    ordering = ['part_of_speach', 'weight', ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
    }


class WordAdmin(admin.ModelAdmin):
    search_fields = ['word']
    ordering = ['-modified', ]
    list_display = ('word', 'transcription', 'audio', 'created', 'modified', )
    list_filter = ('is_oxford_3000', )
    inlines = [
        DefinitionInline,
    ]
    
admin.site.register(Word, WordAdmin)
admin.site.register(Definition, DefinitionAdmin)
