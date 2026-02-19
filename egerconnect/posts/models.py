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
    
