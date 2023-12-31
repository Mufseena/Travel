from django.db import models


# Create your models here.
class travel(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    desc = models.TextField()

    def __str__(self):
        return self.name


class travel_team(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    desc = models.TextField()

    def __str__(self):
        return self.name
