from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from sorl.thumbnail import ImageField, get_thumbnail
from django.urls import reverse


class BlogPost(models.Model):
    class Meta:
        ordering = ['created_at']

    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='blog_posts', blank=True, null=True)
    slug = models.CharField(max_length=300)
    published = models.BooleanField(blank=True, default=False)
    hero_image = ImageField(upload_to='blog/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def get_meta_data(self, request):
        truncator = Truncator(strip_tags(self.content))
        description = truncator.words(35)
        image = ''

        full_domain = '{}://{}'.format(settings.META_SITE_PROTOCOL, settings.META_SITE_DOMAIN)

        if self.hero_image:
            thumbnail = get_thumbnail(self.hero_image, '900x350', crop='center')
            image = '{}{}'.format(full_domain, thumbnail.url)

        url = '{}{}'.format(full_domain, self.get_absolute_url())

        return {
            'type': 'article',
            'title': self.title,
            'description': description,
            'image': image,
            'url': url,
        }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post', args=[self.slug])


@receiver(pre_save, sender=BlogPost)
def pre_save_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

    if instance.published and not instance.published_at:
        instance.published_at = timezone.now()
    elif not instance.published:
        instance.published_at = None
