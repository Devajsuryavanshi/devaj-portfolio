from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=100)
    date = models. DateField()
    url = models.URLField()
    content = models.TextField()
    image = models.ImageField(upload_to = 'blog_image')