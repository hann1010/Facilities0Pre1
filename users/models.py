from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    members_of = models.CharField(max_length=200, blank=True)
    user_level= models.IntegerField(default=1)
    list_rows= models.IntegerField(default=10)
    
    def __str__(self):
        return  str(self.user) + " / " + str(self.user_level) + " / " \
            + self.members_of + " / " + str(self.list_rows)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()