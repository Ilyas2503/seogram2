from django.db import models
from main.models import Post


class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True)
    message = models.TextField()

# Create your models here.
