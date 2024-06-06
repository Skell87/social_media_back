from django.contrib import admin
from social_media_back_app.models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

class UserPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserPost, UserPostAdmin)