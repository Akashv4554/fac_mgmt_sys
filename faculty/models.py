from django.db import models

# Create your models here.

class FacultyMember(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    designation = models.CharField(max_length=50, default="Professor")
    qualifications = models.CharField(max_length=200, default='Not Provided')
    specialization = models.CharField(max_length=200, default='Not Provided')
    contact_no = models.CharField(max_length=20, default='0000000000')
    experience = models.CharField(max_length=20, default="0 years")
    img = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
