from django.shortcuts import render, get_object_or_404,redirect
from .models import Movie,Comment,Favorite
from django.urls import reverse
from .forms import ImageForm,CommentForm,EditForm,FavoriteForm
from django.utils import timezone
from django.views.generic import TemplateView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


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

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def delete(request, pk):
    movie = get_object_or_404(Movie,pk=pk)
    movie.delete()
    return redirect('toppage')

@login_required(login_url='/accounts/login/')
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

def logout_view(request):
    logout(request)
    return redirect('toppage')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('toppage')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def favorites(request):
    if request.method == 'GET':
        page_num = request.GET.get('p', 1)
        pagenator = Paginator(Movie.objects.all().order_by('-created_date'),20)
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
    return render(request, 'favorites.html', ctx)

def favorite(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = FavoriteForm(request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.movie = movie
            favorite.save()
            return redirect('favorites', pk=pk)
    else:
        form = FavoriteForm()
    return render(request, 'favorites.html', {'form': form})
        


# Create your views here.