from django.db import models

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    city=models.CharField(max_length=300)
    content=models.TextField()
    TimeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'message from '+ self.name