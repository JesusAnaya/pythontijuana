from django.views.generic import ListView, DetailView
from blog.models import BlogPost


class BlogPostsList(ListView):
    template_name= 'blog/blog_posts_list.html'
    model = BlogPost
    queryset = BlogPost.objects.filter(published=True)
    paginate_by = 10
    context_object_name = 'blog_posts_list'


class BlogPost(DetailView):
    template_name= 'blog/blog_post.html'
    model = BlogPost
    queryset = BlogPost.objects.filter(published=True)
    context_object_name = 'blog_post'
