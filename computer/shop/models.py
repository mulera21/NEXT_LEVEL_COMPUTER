from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    more = models.CharField(max_length=2500)
    image = models.FileField(upload_to="projects", blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
