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
    following = models.ManyToManyField(
        'User', related_name='user_following_list')

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    plot = models.TextField(max_length=1000)
    cast = models.CharField(max_length=255, blank=True)
    poster = models.URLField()
    rated = models.CharField(max_length=10)
    director = models.CharField(max_length=255)
    date_released = models.CharField(max_length=255)
    roten_score = models.CharField(max_length=10)

    # added
    run_time = models.CharField(max_length=255)
    imdbId = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()

    # relationships
    likes = models.ManyToManyField(User, related_name='user_movie_likes')
    watched = models.ManyToManyField(User, related_name='user_movie_watched')
    watch_list = models.ManyToManyField(
        User, related_name='user_movue_watch_list')

    def __str__(self):
        return f'{self.title}({self.year})'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_movie_review')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='movie_reviews')
    review = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.movie.title}({self.user.first_name})'