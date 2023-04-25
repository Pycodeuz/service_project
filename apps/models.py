from django.db import models
import uuid


class Event(models.Model):
    _id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False)
    details = models.TextField()
    years_ago = models.PositiveIntegerField()


