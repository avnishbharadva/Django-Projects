from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    class Meta:
        db_table = "studentData"