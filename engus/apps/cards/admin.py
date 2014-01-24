from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'status', 'created', 'level', )
    readonly_fields = ('word', )


admin.site.register(Card, CardAdmin)
