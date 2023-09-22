from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Category

# Create your views here.
#home page for logged in users
def home(request):
    posts = Post.objects.all()[0:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {
        'posts':posts,
        'tags':tags,
        'categories':categories,
        'title':'Recent Updates'
    }
    return render(request, 'dashboard/home.html', context)

#detailed post

def detail_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    tag = Post.objects.filter(tag=True)
    context = {
        'post':post,
        'tag':tag
    }
    
    return render(request, 'dashboard/detail.html', context)

#register new user
def register_user(request):
    return render(request, 'dashboard/register.html', {})



#login registered users
def login_user(request):
    return render(request, 'dashboard/login.html', {})


#logout users
def logout_user(request):
    return render(request, 'dashboard/logout.html', {})



