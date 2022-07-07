from django.shortcuts import render
from django.views.generic import CreateView
from .forms import PostForm
from .models import Post
from django.urls import reverse

def home(request):
    post_objects = Post.objects.order_by('-id')
    context = {'post_objects' : post_objects}
    return render(request, 'index.html', context)

def team_intro(request):
    return render(request, 'backend_team.html')

def post_list(request):
    post_objects = Post.objects.order_by('-id')
    context = {'post_objects' : post_objects}
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    post_detail_object = Post.objects.get(pk=pk)
    context = {'post_detail_object' : post_detail_object}
    return render(request, 'post_detail.html', context)

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = '/post_list/'

def company_list(request):
    return render(request, 'company_list.html')

def company_detail(request):
    return render(request, 'company_detail.html')