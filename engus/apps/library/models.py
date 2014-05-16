from django.db import models
from engus.apps.dictionary.models import Word


class Material(models.Model):
    MOVIES = 'movies'
    MUSIC = 'music'
    BOOKS = 'books'
    CATEGORY = (
        (MOVIES, 'Movies'),
        (MUSIC, 'Music'),
        (BOOKS, 'Books'),
    )
    name = models.CharField(max_length=255)
    rus_name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="materials_images/%Y_%m_%d", null=True, blank=True)
    subtitles = models.FileField(upload_to="materials_subtitles/%Y_%m_%d", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_number_of_words(self):
        return self.materialword_set.count()


class MaterialWord(models.Model):
    word = models.ForeignKey(Word)
    material = models.ForeignKey(Material)
    frequency = models.PositiveIntegerField()

    class Meta:
        unique_together = (("word", "material"), )
        ordering = ["-frequency", ]