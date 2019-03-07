from django.utils import timezone
from django.contrib import admin
from django.db import models
from django import forms
from events.models import Event, Organization


class Bed(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    bed_type = models.CharField(max_length=50)
    initial_num_available = models.IntegerField
    num_used = models.IntegerField
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.org_name)
