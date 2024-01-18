from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    content=models.TextField()
    blogtype=models.CharField(max_length=100,blank=True)
    slug=models.CharField(max_length=150)
    TimeStamp=models.DateTimeField(blank=True)
    def __str__(self):
        return self.title + ' by ' + self.author




