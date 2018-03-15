from django.conf.urls import url, include
from .views import *
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    url(r'^post_list/$', get_post_list, name='post_list'),
    url(r'^post_details/(\d+)$', get_post_details, name='post_details'),
    url(r'^edit_post/(\d+)$', edit_post, name='edit_post'),
    url(r'^posts/create', create_post, name='create_post'),
]