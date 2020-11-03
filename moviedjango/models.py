from django.db import models
from django.utils import timezone



class Movie(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    overview = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now) #models.DateTimeField(blank=True, null=True)
    movies = models.FileField(upload_to='images/', blank=False, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=20)
    text = models.TextField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.text


# Create your models here.
