from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'created', 'level', )


admin.site.register(Card, CardAdmin)
