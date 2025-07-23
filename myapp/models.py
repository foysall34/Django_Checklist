from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
   


# class MediaItem(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(blank=True, null= True)

#     def __str__(self):
#         return self.name
