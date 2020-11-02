from django.shortcuts import render, get_object_or_404,redirect
from .models import Movie,Comment
from django.urls import reverse
from .forms import ImageForm,CommentForm,EditForm
from django.utils import timezone
from django.views.generic import TemplateView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def toppage(request):
    if request.method == 'GET':
        page_num = request.GET.get('p', 1)
        pagenator = Paginator(Movie.objects.all().order_by('-published_date'),20)
        try:
            page = pagenator.page(page_num)
        except PageNotAnInteger:
            page = pagenator.page(1)
        except EmptyPage:
            page = pagenator.page(pagenator.num_pages)
        
        ctx = {
            'page_obj': page,
            'movies': page.object_list,
            'is_paginated': page.has_other_pages}
    return render(request, 'toppage.html', ctx)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie,pk=pk)
    comments = Comment.objects.filter(movie = movie)
    return render(request, 'movie_detail.html', {'movie': movie, 'comments':comments})

def movie_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.published_date = timezone.now()
            movie.movies = request.FILES['movies']
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = ImageForm()
    return render(request, 'movie_form.html', {'form': form})

def movie_comment(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('movie_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'movie_comment.html', {'form': form})

def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('toppage')

def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.published_date = timezone.now()
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = EditForm(instance=movie)
    return render(request, 'movie_edit.html', {'form': form})


# Create your views here.