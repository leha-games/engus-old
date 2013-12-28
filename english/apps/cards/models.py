from django.db import models
from django.contrib.auth.models import User
from english.apps.dictionary.models import Word


class Card(models.Model):
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    created = models.DateTimeField(auto_now_add=True)
    repeat = models.DateTimeField(null=True, blank=True)
    next_repeat = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'word') 
