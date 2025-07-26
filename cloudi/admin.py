from django.contrib import admin

# Register your models here.
from .models import MediaItem, APIUser

admin.site.register(MediaItem)
admin.site.register(APIUser)