from django import forms
from .models import Movie,Comment,Favorite
from django.forms import ModelForm, Textarea, Select

class ImageForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('author', 'title','movies', 'overview','published_date')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': Textarea(attrs={'cols': 10, 'rows': 20}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'overview','published_date')

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('user', 'created_date', 'movie')