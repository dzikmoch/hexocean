from django.db import models
from django.contrib.auth.models import User


class Tier(models.Model):
    name = models.CharField(default='basic', max_length=50, blank=False)
    thumbnail_size = models.CharField(max_length=100, blank=True)
    link_orig = models.BooleanField(blank=True)
    link_expir = models.BooleanField(blank=True)

    def __str__(self) -> str:
        return f'Name: {self.name}; thumbnail sizes: {self.thumbnail_size}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, null=True)

