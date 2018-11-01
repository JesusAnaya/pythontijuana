from django.urls import path
from blog.views import BlogPostsList, BlogPost


urlpatterns = [
    path('', BlogPostsList.as_view(), name='blog'),
    path('<slug:slug>/', BlogPost.as_view(), name='blog-post'),
]
