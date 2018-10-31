from django.urls import path
from blog.views import BlogPostsList


urlpatterns = [
    path('', BlogPostsList.as_view(), name='blog'),
]
