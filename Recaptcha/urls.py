from .import views
from django.urls import path


urlpatterns = [
    path('comments/', views.comments, name='comments'),
    ]