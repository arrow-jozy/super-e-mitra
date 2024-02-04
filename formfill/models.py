from django.db import models
from django.utils import timezone




# Create your models here.





class Formfill(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    guiders=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    city=models.CharField(max_length=300)
    form_name=models.TextField()
    # pdf_files = models.FileField()
    TimeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'message from '+ self.name


class UserformImage(models.Model):
    userform = models.ForeignKey(Formfill, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='userform_photos/')
    # Additional fields if needed, like caption, description, etc.

    def __str__(self):
        return f'Image by {self.userform.name}'



