from django.urls import path
from .views import HomePage, DetailPostView, CreatePostView, UpdatePostView


urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('/detail/<int:pk>', DetailPostView.as_view(), name='detail-post-page'),
    path('/create', CreatePostView.as_view(), name='create-post-page'),
    path('/update/<int:pk>', UpdatePostView.as_view(), name='update-post-page'),
]