from django.urls import path
from .views import PostView, PosttView

urlpatterns = [
    path('posts/', PostView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PosttView.as_view(), name='post-detail'),
]