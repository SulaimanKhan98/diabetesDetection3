from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Enum for user type
class TypeOfUser(models.TextChoices):
    PATIENT = 'Patient', 'Patient'
    DOCTOR = 'Doctor', 'Doctor'

# Custom User Model
class User(AbstractUser):
    type_of_user = models.CharField(max_length=200, choices=TypeOfUser.choices, default=TypeOfUser.PATIENT)
    BLOOD_GROUPS = [
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    ]
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)

    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField(blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True)
    address = models.CharField(max_length=500, blank=True)

# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise ValidationError("User Already Exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email Already Exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Appointment Model
class Appointment(models.Model):
    user_ho_add = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ho_add_appointment')
    patient = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='patient_app')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_app')
    date = models.DateField(null=False, blank=False, default=timezone.now)
    start_time = models.TimeField(null=True, blank=True, default=timezone.now)
    end_time = models.TimeField(null=True, blank=True, default=timezone.now)

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    link = models.URLField(blank=True, null=True)
    read = models.BooleanField(default=False)

# Blogs Model
STATUS = [
    (0, 'Draft'),
    (1, 'Published'),
]

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

# Patient Medical_File Models
class MedicalFile(models.Model):
    patient = models.ForeignKey(User, related_name='medical_files', on_delete=models.CASCADE)
    date = models.DateField()
    diagnostic = models.CharField(max_length=255)

# Patient Model (Consider renaming to avoid confusion with the User model)
class Patient(models.Model):
    name = models.CharField(max_length=255)
    blood_sugar_test = models.CharField(max_length=255)
    glucose_screening_test = models.CharField(max_length=255)
    a1c_test = models.CharField(max_length=255)
