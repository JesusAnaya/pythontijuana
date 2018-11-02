from django.views.generic import ListView, DetailView
from blog.models import BlogPost


class BlogPostsList(ListView):
    template_name= 'blog/blog_posts_list.html'
    model = BlogPost
    paginate_by = 10
    context_object_name = 'blog_posts_list'

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(published=True)


class BlogPost(DetailView):
    template_name= 'blog/blog_post.html'
    model = BlogPost
    context_object_name = 'blog_post'

    def get_context_data(self, **kwargs):
        context = super(BlogPost, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().get_meta_data(self.request)
        return context

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(published=True)
