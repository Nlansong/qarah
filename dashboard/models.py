from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
        
class Post(models.Model):
    title = models.CharField(max_length=255,unique=True)
    excerpt = models.CharField(max_length=160, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    
    class Meta:
        ordering = ['-publish_date']
        
    def __str__(self):
        return self.title
