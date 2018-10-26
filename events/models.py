from django.db import models


class Event(models.Model):
    class Meta:
        ordering = ['start_datetime']

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    venue_name = models.CharField(max_length=255, blank=True, null=True)
    venue_map_url = models.URLField(blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.title
