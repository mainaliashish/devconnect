from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
# importing decorator
# from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

# implementation of signals (just like query callbacks in rails)
# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile saved!')
#     print(f"Instance : {instance}")
#     print(f"Created: {created}")

# def profileDeleted(sender, instance, created, **kwargs):
#     print('Deleting user profile')


# create user profile when a new user is created
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

        # send email after a user profile is created
        subject = "Welcome to Dev Search community"
        message = "We are glad you are here."

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )




def updateUser(sender, instance, created, **kwargs):
   profile = instance
   user = profile.user
   if not created:
    user.first_name = profile.name
    user.username = profile.username
    user.email = profile.email
    user.save()


def deleteUser(sender, instance, created, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=User)

# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(profileDeleted, sender=Profile)

# Using decorator for signals

# @receiver(post_save, sender=Profile)
# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile saved!')
#     print(f"Instance : {instance}")
#     print(f"Created: {created}")
