
from django.db import models
from cloudinary.models import CloudinaryField

class MediaItem(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image') 
    title = models.CharField(max_length=255 , default='Untitled')
    video = models.URLField(blank=True , null= True)  
    document = models.URLField(blank= True , null= True)  
   

    def __str__(self):
        return self.name
