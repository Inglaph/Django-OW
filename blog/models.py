from django.db import models


class Post(models.Model):
    """Modelo de Post."""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        """Meta options."""
        app_label = 'blog'

    def __str__(self):
        return self.title
  