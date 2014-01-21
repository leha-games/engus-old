import datetime
from django.db import models
from django.contrib.auth.models import User

TRIAL_DAYS = 14

class Profile(models.Model):
    user = models.OneToOneField(User)
    is_english_mode = models.BooleanField(default=False)
    paid_till = models.DateField(default=lambda: datetime.datetime.now() + datetime.timedelta(days=TRIAL_DAYS))
    
    def __unicode__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)

models.signals.post_save.connect(create_profile, sender=User)
