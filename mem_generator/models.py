from django.db import models


class Musician(models.Model):
    path = models.ImageField()
    title = models.CharField(max_length=128)