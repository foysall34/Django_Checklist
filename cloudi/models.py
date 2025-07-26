
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings

class MediaItem(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image') 
    title = models.CharField(max_length=255 , default='Untitled')
    video = models.URLField(blank=True , null= True)  
    document = models.URLField(blank= True , null= True)  
   

    def __str__(self):
        return self.name


# For logMeal 
class APIUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='api_tokens')
    username = models.CharField(max_length=100)
    token = models.CharField(max_length=255)
    is_enabled = models.BooleanField(default=True)
    language = models.CharField(max_length=50, default='English')

    def __str__(self):
        return f"{self.username} - {self.user.email}"