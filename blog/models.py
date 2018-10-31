from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=300)
    published = models.BooleanField(blank=True, default=False)
    hero_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.title
