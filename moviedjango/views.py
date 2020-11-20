from django.shortcuts import render, get_object_or_404,redirect
from .models import Movie,Comment
from django.urls import reverse
from .forms import ImageForm,CommentForm,EditForm,FavoriteForm
from django.utils import timezone
from django.views.generic import TemplateView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
import boto3
import os
import datetime


@login_required(login_url='/accounts/login/')
def toppage(request):
    if request.method == 'GET':
        page_num = request.GET.get('p', 1)
        pagenator = Paginator(Movie.objects.prefetch_related('favorite_set').all().order_by('-published_date'), 20)
        try:
            page = pagenator.page(page_num)
            movies = page.object_list
            faveored_or_not = [movie.favored_by(request.user) for movie in movies]
        except PageNotAnInteger:
            page = pagenator.page(1)
        except EmptyPage:
            page = pagenator.page(pagenator.num_pages)
        ctx = {
            'page_obj': page,
            'movies': [(movie,favorite) for movie,favorite in zip(movies,faveored_or_not)],
            'is_paginated': page.has_other_pages,}
    return render(request, 'toppage.html', ctx)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie,pk=pk)
    faveored_or_not = movie.favored_by(request.user)
    comments = Comment.objects.filter(movie = movie)
    return render(request, 'movie_detail.html', {'movie':movie, 'comments':comments, 'faveored': faveored_or_not})

@login_required(login_url='/accounts/login/')
def movie_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.published_date = timezone.now()
            url = for_s3(request)
            movie.movies = url
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
        form = EditForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.published_date = timezone.now()
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = EditForm()
    return render(request, 'movie_edit.html', {'form': form, 'movie': movie})

def logout_view(request):
    logout(request)
    return redirect('toppage')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('toppage')
    else:
        form = UserCreationForm()
    print(dir(form.error_messages.values.__text_signature__))
    return render(request, 'signup.html', {'form': form})

def favorites(request):
    movies = Movie.objects.all().order_by('-published_date')
    faveored_or_not = [movie.favored_by(request.user) for movie in movies]
    dic = {'movies': [(movie,favorite) for movie,favorite in zip(movies,faveored_or_not)]}
    return render(request, 'favorites.html', dic)

def favorite(request, pk):
    if request.method != 'POST':
        return HttpResponse('only POST request allowed.', status=405)

    movie = get_object_or_404(Movie, pk=pk)
    if movie.favored_by(request.user):
        movie.disfavor(request.user)
    else:
        movie.favor(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def search(request):
    movies = Movie.objects.order_by(-published_date)
    keyword = request.GET.get('keyword')
    if keyword:
        movies = movies.filter(Q(title__icontains=keyword))
        messages.success(request,'「{}」のMOVIES'.format(keyword))
    return render(request, 'toppage.html', {'movies': movies})


def for_s3(request):
    d = datetime.datetime.now()
    filename = f'movie{d}.mp4'
    sess = boto3.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
    s3 = sess.client('s3')
    s3.put_object(Bucket='moviedjango', Body=request.FILES['movies'], Key=filename, ACL='public-read')
    return f'https://moviedjango.s3-ap-northeast-1.amazonaws.com/{filename}'





# Create your views here.