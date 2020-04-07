# this file is made so that whenever we have a new user
#that will sign up his profile page is made automatically
#by firing the post_save after the user is created
# post_save is the signal that is fired from django signals
# after editing this file make sure to add this file in 
#the users apps.py file because the documentation of the 
#django file says so 

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

def save_profile(sender, instance, **kwargs):
    instance.profile.save()