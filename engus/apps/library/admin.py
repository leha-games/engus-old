from django.contrib import admin
from .models import Material, MaterialWord
from .utils import find_words, save_material_words


def create_film_words(modeladmin, request, queryset):
    for film in queryset:
        words = find_words(film.subtitles.file)
        save_material_words(film, words)


class FilmAdmin(admin.ModelAdmin):
    readonly_fields = ['get_number_of_words', ]
    list_display = ('name', 'get_number_of_words', )
    prepopulated_fields = {"slug": ("name",)}
    actions = [create_film_words, ]


class FilmWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'material', 'frequency', )


admin.site.register(Material, FilmAdmin)
admin.site.register(MaterialWord, FilmWordAdmin)