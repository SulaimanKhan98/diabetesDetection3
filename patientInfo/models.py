from django.db import models

class PatientHistory(models.Model):
    
    age = models.IntegerField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    prediction_result = models.BooleanField(null=True, blank=True)

class PatientDetails(models.Model):

    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cnic = models.BigIntegerField()
    number = models.BigIntegerField()

class Doctor(models.Model):

   
    name = models.CharField(max_length=255)
    cnic = models.BigIntegerField()
    number = models.BigIntegerField()