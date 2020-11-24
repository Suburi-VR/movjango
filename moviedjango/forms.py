from django import forms
from django.forms import Select, Textarea, TextInput
from .models import Movie, Comment, Favorite

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
        fields = ('author', 'title', 'overview','published_date')
        widgets = {
                'author': Select(attrs={
                    'class': "form-control",
                    'disabled': True, 
                }),
                'title': TextInput(attrs={
                    'class': "form-control",
                }),
                'overview': Textarea(attrs={
                    'class': "form-control",
                    'rows': 7,
                    'maxlength': 500
                }),
                'published_date': TextInput(attrs={
                    'class': "form-control",
                    'disabled': True,
                }),
        }

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('user', 'created_date', 'movie')