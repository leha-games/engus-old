from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    is_english_mode = models.BooleanField(default=False)
    learn_by = models.IntegerField(default=7)
    
    def __unicode__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)

models.signals.post_save.connect(create_profile, sender=User)
