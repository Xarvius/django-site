from django.contrib import admin
from user_manage.models import UserProfile, UserFolder, UserFiles

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserFolder)
admin.site.register(UserFiles)
