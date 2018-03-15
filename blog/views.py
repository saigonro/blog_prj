from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, EditPostForm
from django.utils import timezone

# Create your views here.

def get_post_list(request):
    items = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'items': items})
    
def get_post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, 'blog/post_details.html', {'post': post})

def create_post(request):
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('home')
    else:
        form = PostForm()
    
    return render(request, "blog/create_post.html", { 'form': form })
    
def edit_post(request, id): 
    edit_post = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=edit_post)
        if form.is_valid():
            edit_post=form.save(commit=False)
            edit_post.author=request.user
            edit_post.save()
            return redirect(get_post_details,edit_post.pk)
    else:
        print("It's the GET")
        
    form = EditPostForm(instance=edit_post)
    return render(request, "blog/edit_post.html", {'form': form})
