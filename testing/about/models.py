from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class AboutUs(models.Model):
    title=models.CharField(max_length=100)
    about_data=HTMLField()
