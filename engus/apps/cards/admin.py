from django.contrib import admin
from .models import Card

def set_status_to_new(modeladmin, request, queryset):
    queryset.update(status=0)

class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'status', 'created', 'level', )
    readonly_fields = ('word', )
    actions = [set_status_to_new]


admin.site.register(Card, CardAdmin)
