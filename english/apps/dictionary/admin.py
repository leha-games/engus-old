from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Word, Definition


class DefinitionInline(admin.StackedInline):
    model = Definition
    extra = 0
    ordering = ['part_of_speach', 'weight', ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
    }


class WordAdmin(admin.ModelAdmin):
    search_fields = ['word']
    ordering = ['modified', ]
    list_display = ('word', 'transcription', 'public', 'created', 'modified', )
    inlines = [
        DefinitionInline,
    ]
    
admin.site.register(Word, WordAdmin)
