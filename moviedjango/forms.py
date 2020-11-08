from django import forms
from .models import Movie
from .models import Comment
from .models import Favorite

class ImageForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('author', 'title','movies', 'overview','published_date')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

class EditForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'overview','published_date')

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('movie', 'created_date', 'user')