from django.contrib.auth.models import User, AbstractBaseUser
from django.utils import timezone
from django.db import models

class Organization(models.Model):
    org_type = models.CharField(max_length=25)
    org_name = models.CharField(max_length=250)
    org_addr1 = models.CharField(max_length=250)
    org_addr2 = models.CharField(max_length=250)
    org_city = models.CharField(max_length=150)
    org_state = models.CharField(max_length=5)
    org_zip = models.CharField(max_length=10)
    org_primary_phone = models.CharField(max_length=25)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.org_name)

class Nurse(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    phone = models.CharField(max_length=25)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name


# Create your models here.
class Event(models.Model):
    event_type = models.CharField(max_length=25)
    event_description = models.CharField(max_length=250, blank=True)
    event_start_date = models.DateTimeField
    event_end_date = models.DateTimeField
    simulation_flag = models.BooleanField
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.event_description)