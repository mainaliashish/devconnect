from django.contrib import admin
from . models import Profile, Skill, Message
# Register your models here.

admin.site.register([Profile, Skill, Message])
