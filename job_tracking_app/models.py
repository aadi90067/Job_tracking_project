from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=200)

class JobApplications   (models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ]

    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ no extra space here

    def __str__(self):
        return f"{self.job_title} at {self.company}"



