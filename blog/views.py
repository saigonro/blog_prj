from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def get_post_list(request):
    items = Post.objects.all()
    return render(request, 'blog/post_list.html', {'items': items})
    
def get_post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post_details.html', {'post': post})
