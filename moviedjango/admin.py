from django.contrib import admin
from .models import Movie, Comment, Favorite, Tag

admin.site.register(Comment)
admin.site.register(Movie)
admin.site.register(Favorite)
admin.site.register(Tag)

# Register your models here.
