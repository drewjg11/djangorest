from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    owner = models.CharField(max_length=50, default=creator)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25, null=False)
    description = models.CharField(max_length=250, null=False, default="Enter company description")
    category = models.CharField(max_length=40, null=True)
    industry = models.CharField(max_length=25, null=False, default="")
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.name