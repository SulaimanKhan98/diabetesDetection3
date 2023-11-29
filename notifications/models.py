# models.py in notifications app

from django.db import models

class Notification(models.Model):
    user_id = models.IntegerField()  # Replace with ForeignKey(UserProfile, on_delete=models.CASCADE) if using user profiles
    message = models.TextField()
    link = models.URLField(blank=True, null=True)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
