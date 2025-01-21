from django.db import models as m
from uuid import uuid4 as u4

class Order(m.Model):
    uid = m.UUIDField(default=u4, unique=True)
    link = m.URLField(unique=True)  # Ensures no duplicate links
    title = m.CharField(max_length=255)  # Title of the task
    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.link}"