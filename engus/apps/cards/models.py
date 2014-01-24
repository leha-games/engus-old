from django.db import models
from django.contrib.auth.models import User
from engus.apps.dictionary.models import Word


class Card(models.Model):
    NEW = 0
    LATER = 1
    LEARNED = 2
    STATUS_CHOICES = (
        (NEW, 'new'),
        (LATER, 'later'),
        (LEARNED, 'learned'),
    )
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    created = models.DateTimeField(auto_now_add=True)
    level = models.PositiveIntegerField(default=0)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=NEW)

    class Meta:
        unique_together = ('user', 'word') 
