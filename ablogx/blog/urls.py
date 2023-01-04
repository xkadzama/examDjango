from django.urls import path
from .views import HomePage, DetailPostView


urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('/detail/<int:pk>', DetailPostView.as_view(), name='detail-post-page'),
]