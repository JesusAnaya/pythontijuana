from django.utils import timezone
from django import template
from events.models import Event
from blog.models import BlogPost

register = template.Library()


@register.inclusion_tag('templatetags/home_next_event.html')
def next_event():
    now = timezone.now()
    next_event = Event.objects.filter(end_datetime__gte=now).first()

    return {
        'next_event': next_event,
    }


@register.inclusion_tag('templatetags/home_blog_posts.html')
def home_blog_posts():
    blog_posts = BlogPost.objects.filter(published=True)[:3]

    return {
        'blog_posts_list': blog_posts,
    }
