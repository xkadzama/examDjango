from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForms, UpdateForms
from django.urls import reverse_lazy

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


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = UpdateForms


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home-page')
    