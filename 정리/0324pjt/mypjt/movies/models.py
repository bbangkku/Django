from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre_menu = (('코미디','코미디'),('공포','공포'),('로맨스','로맨스'))
    genre = models.CharField(max_length=30,choices=genre_menu)
    score = models.IntegerField(validators=(MinValueValidator(0), MaxValueValidator(5),))
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField(blank=True, null=True)