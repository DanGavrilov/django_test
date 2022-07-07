from django.urls import path
from django.views.generic import ListView

from . import views
from .models import Post

urlpatterns = [
   path('register', views.register, name='register'),
   path('', views.log_in, name='login'),
   path('logout', views.log_out, name='logout'),
   path('profile', views.profile, name='profile'),
   path('create_post', views.create_post, name='create_post')
]