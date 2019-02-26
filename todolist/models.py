from django.db import models
from django.conf import settings

class Todo(models.Model):
    item = models.TextField()
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank = False,
        null = True
    )

    def __str__(self):
        return self.item



