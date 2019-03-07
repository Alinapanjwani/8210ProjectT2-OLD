from django.db import models
from django.utils import timezone
from events.models import Event, Organization

# Create your models here.
class Patient(models.Model):
    patient_last_name = models.CharField(max_length=150)
    patient_first_name = models.CharField(max_length=150)
    patient_middle_name = models.CharField(max_length=150, blank=True)
    age = models.IntegerField(blank=True)
    dob = models.DateTimeField(blank=True)
    gender = models.CharField(max_length=5,blank=True)
    unique_characteristics = models.CharField(max_length=1000,blank=True)
    next_of_kin_name = models.CharField(max_length=250,blank=True)
    next_of_kin_relation = models.CharField(max_length=150, blank=True)
    next_of_kin_phone = models.CharField(max_length=25, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.patient_first_name + ' ' + self.patient_last_name)


class PatientTrackingHeader(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    original_updated = models.CharField(max_length=5)
    street_address = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    submitted_date = models.DateTimeField(blank=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.street_address + ' ' + str(self.org_id))


class PatientTrackingDetail(models.Model):
    tracking_id = models.ForeignKey(PatientTrackingHeader, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    triage_tag_num = models.CharField(max_length=50, blank=True)
    tag_color_condition = models.CharField(max_length=25, blank=True)
    mode_of_arrival = models.CharField(max_length=25, blank=True)
    room_number = models.CharField(max_length=25, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    arrival_date = models.DateTimeField(blank=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return (str(self.tracking_id) + ' ' + str(self.patient_id))


class PatientTrackingInjuries(models.Model):
    tracking_detail_id = models.ForeignKey(PatientTrackingDetail, on_delete=models.CASCADE)
    injury_type = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return (str(self.tracking_detail_id) + ' ' + self.injury_type)


class PatientTrackingDisposition(models.Model):
    tracking_detail_id = models.ForeignKey(PatientTrackingDetail, on_delete=models.CASCADE)
    disposition_type = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=500, blank=True)
    transfer_to_org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    time_of_death = models.DateTimeField
    updated_condition = models.CharField(max_length=25, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return (str(self.tracking_detail_id) + ' ' + self.disposition_type)

