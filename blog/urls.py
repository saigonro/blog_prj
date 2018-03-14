from django.conf.urls import url, include
from .views import *
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    url(r'^post_list/', get_post_list, name='post_list'),
    url(r'^post_details/(\d+)$', get_post_details, name='post_details'),
    # url(r'^post_list/', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="post_list.html")),
]