from django.contrib import admin
from django.urls import path
from .views import BlogView, PublicBlog

urlpatterns = [
    path('blog/', BlogView.as_view()),
    path('', PublicBlog.as_view()),
]