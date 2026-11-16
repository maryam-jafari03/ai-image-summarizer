from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    format = models.TextField()
    size = models.IntegerField()
    dimensions = models.IntegerField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='photos',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.format
