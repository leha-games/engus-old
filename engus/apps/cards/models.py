import datetime
from django.db import models
from django.contrib.auth.models import User
from engus.apps.dictionary.models import Word


class Card(models.Model):
    NEW = 'new'
    LEARNED = 'learned'
    KNOW = 'know'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (LEARNED, 'Learned'),
        (KNOW, 'Know'),
    )
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    created = models.DateTimeField(auto_now_add=True)
    learned = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    when_learned = models.DateTimeField(null=True, blank=True)
    level = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'word') 
        ordering = ['-created', ]

    def save(self, *args, **kw):
        if self.pk is not None:
            orig = Card.objects.get(pk=self.pk)
            if orig.status != Card.LEARNED and self.status == Card.LEARNED:
                self.when_learned = datetime.datetime.now()
            elif orig.status != Card.NEW and self.status == Card.NEW:
                self.when_learned = None
        super(Card, self).save(*args, **kw)
