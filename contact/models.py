from django.db import models


class Contact(models.Model):
    First_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Subject = models.CharField(max_length=200)
    Message = models.TextField()

# Create your models here.
