from django.db import models
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.TextField(default='학생')
    views = models.IntegerField(default=0)
    image = models.ImageField(blank=True)
    