from django.db import models
from django.contrib.auth.models import User
from english.apps.dictionary.models import Word


class UserWords(models.Model):
    user = models.OneToOneField(User)
    words = models.ManyToManyField(Word)
