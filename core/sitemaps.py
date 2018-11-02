from django.contrib import sitemaps
from django.conf import settings
from django.urls import reverse
from blog.sitemaps import BlogSitemap


class PageSitemap(sitemaps.Sitemap):
    priority = 0.4
    changefreq = 'weekly'
    protocol = 'http' if settings.DEBUG else 'https'

    def items(self):
        return ['home', 'blog']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'pages': PageSitemap,
    'blog': BlogSitemap,
}
