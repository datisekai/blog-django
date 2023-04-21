from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.name
    class Meta:
        permissions = [
            ("view_my_posts","Can view your posts")
        ]

class Comments(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.content
    class Meta:
        default_permissions = []
  

class Reacts(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    icon = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.icon
    class Meta:
        default_permissions = []
   
class StatisticalBase(models.base.ModelBase):
    def save(self, *args, **kwargs):
        # do nothing
        pass

    def delete(self, *args, **kwargs):
        # do nothing
        pass

class Statistical(models.Model,metaclass=StatisticalBase):
    class Meta:
        managed = False
        verbose_name_plural = 'Statisticals'