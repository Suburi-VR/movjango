from django.shortcuts import render, get_object_or_404,redirect
from .models import Movie,Comment
from django.urls import reverse
from .forms import ImageForm,EditForm,CommentForm
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
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.template.loader import render_to_string
import sys
import json




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

@csrf_exempt
def movie_detail(request, pk):
    movie = get_object_or_404(Movie,pk=pk)
    faveored_or_not = movie.favored_by(request.user)
    comments = Comment.objects.filter(movie = movie).order_by('-created_date')
    form = CommentForm(request.POST)
    return render(request, 'movie_detail.html', {'movie': movie, 'comments': comments, 'favored': faveored_or_not, 'form': form})

@login_required(login_url='/accounts/login/')
def comment_send(request, pk):
    movie = get_object_or_404(Movie,pk=pk)
    comment = Comment()
    comment.movie = movie
    comment.author = request.user
    comment.text = json.loads(request.body)
    comment.save()
    return HttpResponse("ww")

def comment_delete(request, id):
    comment = get_object_or_404(Comment,id=id)
    

@login_required(login_url='/accounts/login/')
def movie_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            url = for_s3(request)
            movie.movies = url
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = ImageForm()
    return render(request, 'movie_form.html', {'form': form})

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
            movie.title = request.POST["title"]
            movie.overview = request.POST["overview"]
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = EditForm(instance=movie)
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
    return render(request, 'signup.html', {'form': form})


def favorites(request):
    if request.method == 'GET':
        page_num = request.GET.get('p', 1)
        pagenator = Paginator(Movie.objects.prefetch_related('favorite_set').filter(favorite__user=request.user).order_by('-published_date'), 20)
        try:
            page = pagenator.page(page_num)
            movies = page.object_list
            faveored_or_not = [movie.favored_by(request.user) for movie in movies]
        except PageNotAnInteger:
            page = pagenator.page(1)
        except EmptyPage:
            page = pagenator.page(pagenator.num_pages)
        dic = {
            'page_obj': page,
            'movies': [(movie,favorite) for movie,favorite in zip(movies, faveored_or_not)],
            'is_paginated': page.has_other_pages,}
    return render(request, 'favorites.html', dic)

@csrf_exempt
def favorite(request, pk):
    if request.method != 'POST':
        return HttpResponse('NG')
    movie = get_object_or_404(Movie, pk=pk)
    if movie.favored_by(request.user):
        movie.disfavor(request.user)
    else:
        movie.favor(request.user)
    return HttpResponse("OK")

def disfav(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if movie.favored_by(request.user):
        movie.disfavor(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if keyword:
            messages.success(request,'「{}」のMOVIES'.format(keyword))
        page_num = request.GET.get('p', 1)
        pagenator = Paginator(Movie.objects.prefetch_related('favorite_set').filter(Q(title__icontains=keyword)|Q(overview__icontains=keyword)).order_by('-published_date'), 20)
        try:
            page = pagenator.page(page_num)
            movies = page.object_list
            faveored_or_not = [movie.favored_by(request.user) for movie in movies]
        except PageNotAnInteger:
            page = pagenator.page(1)
        except EmptyPage:
            page = pagenator.page(pagenator.num_pages)
   
    dic = {
        'page_obj': page,
        'movies': [(movie,favorite) for movie,favorite in zip(movies, faveored_or_not)],
        'is_paginated': page.has_other_pages,
    }
    return render(request, 'search.html', dic)


def for_s3(request):
    d = datetime.datetime.now()
    filename = f'movie{d}.mp4'
    sess = boto3.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
    s3 = sess.client('s3')
    s3.put_object(Bucket='moviedjango', Body=request.FILES['movies'], Key=filename, ACL='public-read')
    return f'https://moviedjango.s3-ap-northeast-1.amazonaws.com/{filename}'

# @csrf_exempt
# def tag(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     print(request.body)
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         tag = form.save(commit=False)
#         tag.save()
#         tag.movies.add(movie)
#     return HttpResponse('{"message": "ok"}')





# Create your views here.