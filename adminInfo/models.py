from django.db import models
from django.utils import timezone

class AdminDetails(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, default=f'admin_{timezone.now().strftime("%Y%m%d%H%M%S")}')
    password = models.CharField(max_length=128)  # Assuming you handle password hashing elsewhere

    def __str__(self):
        return self.t
