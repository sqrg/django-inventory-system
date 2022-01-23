import uuid

from django.db import models

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    is_container = models.BooleanField(default=False)

    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    container = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)