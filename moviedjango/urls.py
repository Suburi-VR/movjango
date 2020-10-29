from django.urls import path
from . import views


urlpatterns = [
    path('', views.toppage, name='toppage'),
    path('movie/movie_form/', views.movie_form, name='movie_form'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:pk>/movie_comment/', views.movie_comment, name='movie_comment'),
    path('movie/<int:pk>/delete/', views.delete, name='delete'),
]