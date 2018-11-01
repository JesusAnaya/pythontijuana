from django.contrib import admin
from django.utils.translation import gettext as _
from django_summernote.admin import SummernoteModelAdmin
from blog.models import BlogPost


class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'published')
    list_editable = ('published',)

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'slug', 'published')
        }),
        (_('Content'), {
            'fields': ('hero_image', 'content'),
        }),
    )


admin.site.register(BlogPost, BlogPostAdmin)
