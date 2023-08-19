from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser

class TourStatus(Enum):
    COMPLETED = 'COMPLETED'
    QUEUED = 'QUEUED'
    STARTED = 'STARTED'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class TaskStatus(Enum):
    ACCEPTED = 'ACCEPTED'
    CANCELLED = 'CANCELLED'
    CLOSED = 'CLOSED'
    COMPLETED = 'COMPLETED'
    ONGOING = 'ONGOING'
    STARTED = 'STARTED'
    WAITING = 'WAITING'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class User(AbstractUser):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,null=True, blank=True)
    password = models.CharField(max_length=255)
    profile_picture = models.BinaryField(null=True, blank=True,editable=True)
    aadhaar_card = models.BinaryField(null=True, blank=True,editable=True)
    pan_card = models.BinaryField(null=True, blank=True,editable=True)
    contact_number = models.CharField(max_length=15,unique=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=50, null=True, blank=True)
    passbook_picture = models.BinaryField(null=True, blank=True,editable=True)
    username = None
    USERNAME_FIELD = 'contact_number'

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.name

class Tour(models.Model):
    
    tour_id = models.CharField(max_length=255,primary_key=True)
    actual_net_amount = models.IntegerField(null=True, blank=True)
    tour_date = models.DateField(null=True, blank=True)
    total_tasks = models.IntegerField(null=True, blank=True)
    completed_tasks = models.IntegerField(null=True, blank=True)
    ongoing_tasks = models.IntegerField(null=True, blank=True)
    rider_name = models.CharField(max_length=255,null=True, blank=True)
    rider_phone = models.CharField(max_length=15,null=True, blank=True)
    tour_status = models.CharField(null=True, blank=True, choices=TourStatus.choices(),max_length = 20)
    tour_start_time = models.DateTimeField(null=True,blank=True)
    tour_end_time = models.DateTimeField(null=True,blank=True)
    dispatch_time = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "locus_tour_brief"

    def __str__(self):
        return self.tour_id
    
class Task(models.Model):
    
    task_id = models.CharField(max_length=255,primary_key=True)
    awb = models.CharField(max_length=255,null=True, blank=True)
    status = models.CharField(null=True, blank=True, choices=TaskStatus.choices(),max_length = 20)
    rider_id = models.CharField(max_length=255,null=True, blank=True)
    rider_name = models.CharField(max_length=255,null=True, blank=True)
    rider_phone = models.CharField(max_length=15,null=True, blank=True)
    task_start_time = models.DateTimeField(null=True,blank=True)
    task_end_time = models.DateTimeField(null=True,blank=True)
    customer_name = models.CharField(max_length=255,null=True, blank=True)
    customer_address = models.CharField(max_length=255,null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "locus_task_brief"

    def __str__(self):
        return self.task_id