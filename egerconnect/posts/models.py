from django.db import models
from django.conf import settings

class Notice(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="notices/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LostAndFound(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="lost_found/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Scholarship(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="scholarships/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="events/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

from django.db import models

class SupportRequest(models.Model):
    # Section 1: Student Details
    full_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50)
    email = models.EmailField()
    faculty = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    # Section 2: Support Request
    type_of_need = models.CharField(max_length=255)
    explanation = models.TextField(max_length=1000)  # 200–300 words is ~1000 chars

    # Section 3: Financial Aid Status
    financial_aid_status = models.CharField(
        max_length=20,
        choices=[
            ("yes", "Yes"),
            ("no", "No"),
            ("in_progress", "In progress"),
        ],
        default="no"
    )

    # Section 4: Verification (Optional)
    proof_document = models.FileField(upload_to="support_proofs/", blank=True, null=True)
    referee_full_name = models.CharField(max_length=255, blank=True)
    referee_registration_number = models.CharField(max_length=50, blank=True)
    referee_faculty = models.CharField(max_length=255, blank=True)
    confirm_student_status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.type_of_need}"
