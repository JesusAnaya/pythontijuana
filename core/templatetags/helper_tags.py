from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def full_uri(context, path):
    request = context['request']
    return request.build_absolute_uri(path)


@register.simple_tag
def google_analytics_id():
    return getattr(settings, 'GOOGLE_ANALYTICS_ID', None)
