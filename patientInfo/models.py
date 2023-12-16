# models.py in patientInfo app

from django.db import models

class PatientDetails(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    cnic = models.BigIntegerField()
    number = models.BigIntegerField()

class PatientData(models.Model):
    patient_details = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    age = models.IntegerField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    prediction_result = models.BooleanField(null=True, blank=True)
    age = models.IntegerField()

