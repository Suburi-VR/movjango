from django import forms
from .models import Movie
from .models import Comment

class ImageForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('author', 'title','movies', 'overview','published_date')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')