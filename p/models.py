from django.db import models as m

from uuid import uuid4 as u4

class Order(m.Model):

    uid = m.UUIDField(default = u4, unique = True)

    title = m.TextField()
    price = m.PositiveSmallIntegerField()

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return f"{self.price}₽ | {self.title}"