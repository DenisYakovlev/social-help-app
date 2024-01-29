from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.TextField(max_length=128, null=True, blank=True, unique=False)
    text = models.TextField(max_length=2048, null=True, blank=True, unique=False)
    support_count = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']