from django.db import models
from django.conf import settings

class Addiction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# models.py (continue)


class UserAddiction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addictions = models.ManyToManyField(Addiction)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} addictions"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addictions = models.ManyToManyField(Addiction)
