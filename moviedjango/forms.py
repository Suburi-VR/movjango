from django import forms
from django.forms import Select, Textarea, TextInput, HiddenInput
from .models import Movie, Comment, Favorite
from django.utils import timezone

class ImageForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title','movies', 'overview','published_date')
        widgets = {
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
                    'readonly': True
                }),
        }


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
        fields = ('author', 'title', 'overview','published_date')
        widgets = {
                'author': HiddenInput(attrs={
                    'class': "form-control"
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
                    'readonly': True
                }),
        }

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('user', 'created_date', 'movie')