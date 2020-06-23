from django.db import models

# Create your models here.
class Project(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=220)
    url = models.URLField(blank = 'true')
    image = models.ImageField(upload_to = 'project_image')