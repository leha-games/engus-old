from django.db import models
from django.contrib.auth.models import User
from english.apps.dictionary.models import Word


class UserWord(models.Model):
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    learning = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    last_repeat = models.DateTimeField(null=True, blank=True)
    repeat_level = models.SmallIntegerField(default=0)
    next_repeat = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'word') 
