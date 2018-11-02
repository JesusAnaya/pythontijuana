from django.contrib.sitemaps import Sitemap
from django.conf import settings
from blog.models import BlogPost


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http' if settings.DEBUG else 'https'

    def items(self):
        return BlogPost.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at
