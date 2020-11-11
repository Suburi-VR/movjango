from django.contrib import admin
from .models import Movie, Comment,Favorite

admin.site.register(Comment)
admin.site.register(Movie)
admin.site.register(Favorite)


# Register your models here.
