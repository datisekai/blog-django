from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return "Name=" + self.name + ",Description=" + self.description
    
class Blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='uploads/')
    category = models.OneToOneField(Categories, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return "Name=" + self.name
    
