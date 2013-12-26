from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
    search_fields = ['word']
    list_display = ('word', 'transcription', 'public', )
    
admin.site.register(Word, WordAdmin)
