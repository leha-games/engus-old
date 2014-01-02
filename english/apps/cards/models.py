from django.db import models
from django.contrib.auth.models import User
from english.apps.dictionary.models import Word


class Card(models.Model):
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    created = models.DateTimeField(auto_now_add=True)
    level = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'word') 
