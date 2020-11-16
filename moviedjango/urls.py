from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.toppage, name='toppage'),
    path('movie/movie_form/', views.movie_form, name='movie_form'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:pk>/movie_comment/', views.movie_comment, name='movie_comment'),
    path('movie/<int:pk>/edit/delete/', views.delete, name='delete'),
    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('movie/<int:pk>/favorite', views.favorite, name='favorite'),
    path('favorites/', views.favorites, name='favorites'),
    path('search/', views.search, name='search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))