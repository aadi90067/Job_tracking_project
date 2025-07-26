from django.contrib import admin
from .models import person
from .models import JobApplications  
# Register your models here.

admin.site.register(person)
admin.site.register(JobApplications)