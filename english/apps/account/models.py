from django.db import models
from django.contrib.auth.models import User
from english.apps.dictionary.models import Word


class UserWord(models.Model):
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    know = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_repeat = models.DateTimeField(null=True, blank=True)
    repeated = models.SmallIntegerField(default=0)
    mistakes = models.SmallIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'word') 
