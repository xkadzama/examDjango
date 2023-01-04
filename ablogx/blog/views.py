from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class HomePage(ListView):
    model = Post
    template_name = 'home.html'


class DetailPostView(DetailView):
    model = Post
    template_name = 'detail.html'