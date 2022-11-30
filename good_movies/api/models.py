from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    # profile_picture = models.ImageField( blank=True)
    date_joined = models.DateField(auto_now=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    plot = models.TextField(max_length=1000)
    cast = models.CharField(max_length=255)
    poster = models.URLField()
    rated = models.CharField(max_length=10)
    director = models.CharField(max_length=255)
    date_released = models.DateField()
    roten_score = models.IntegerField()

    #added
    run_time = models.IntegerField()
    imdbId = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()

    #relationships
    likes = models.ManyToManyField(User, related_name='user_movie_likes')
    watched = models.ManyToManyField(User, related_name='user_movie_watched')
    watch_list = models.ManyToManyField(User, related_name='user_movue_watch_list')

    def __str__(self):
        return f'{self.title}({self.year})'