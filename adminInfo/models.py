from django.db import models

# Create your models here.

class adminDetails(models.Model):

    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    cnic = models.BigIntegerField()
    number = models.BigIntegerField()