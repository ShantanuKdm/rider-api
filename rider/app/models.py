from django.db import models
from django.contrib.auth.models import AbstractUser

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
