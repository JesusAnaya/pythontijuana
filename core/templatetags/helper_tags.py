from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def full_uri(context, path):
    request = context['request']
    return request.build_absolute_uri(path)
