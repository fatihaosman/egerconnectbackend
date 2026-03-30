from django.db import models
from django.contrib.auth.models import User  # built-in user

class SupportRequest(models.Model):
    student_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=50)  # e.g., accommodation, fees
    status = models.CharField(
        max_length=20,
        choices=[('pending','Pending'),('accepted','Accepted'),('declined','Declined')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)  # important for reports

    def __str__(self):
        return f"{self.student_name} - {self.request_type}"