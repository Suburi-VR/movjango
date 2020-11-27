from django.db import models
from django.utils import timezone



class Movie(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    overview = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now) #models.DateTimeField(blank=True, null=True)
    movies = models.FileField(upload_to='images/', blank=False, null=False)
    taggs = models.TextField(max_length=500, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def favored_by(self, user):
        fs = self.favorite_set.filter(user=user)
        return len(fs) == 1

    def favor(self, user):
        favorite = Favorite()
        favorite.movie = self
        favorite.user = user
        favorite.save()

    def disfavor(self, user):
        if not self.favored_by(user):
            return
        fs = self.favorite_set.filter(user=user)
        fs[0].delete()

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, blank=False, null=False)
    author = models.CharField(max_length=20)
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Favorite(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['movie', 'user'], name='duplicate')]

    def __str__(self):
        return f'{str(self.user)} favor in 『{str(self.movie)}』'
        


# Create your models here.
