from django.contrib import admin
from user_manage.models import UserProfile, UserFolder, UserFiles, UserExtras, Results, UserPublications

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserFolder)
admin.site.register(UserFiles)
admin.site.register(UserExtras)
admin.site.register(Results)
admin.site.register(UserPublications)
