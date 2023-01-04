from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForms

class HomePage(ListView):
    model = Post
    template_name = 'home.html'


class DetailPostView(DetailView):
    model = Post
    template_name = 'detail.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForms
    template_name = 'create.html'