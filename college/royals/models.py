from django.db import models
from django.contrib.auth.models import User


class StudentApplication(models.Model):
    student_name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    ssc_percentage= models.CharField(max_length=10)
    inter_percentage= models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)


class Department(models.Model):
    department_name= models.CharField(max_length=30)

    def __str__(self):
        return self.department_name


class Student(models.Model):
    student_application = models.OneToOneField(StudentApplication, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    dob = models.DateField()
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    ssc_percentage = models.CharField(max_length=10)
    inter_percentage = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Staff(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    experience = models.CharField(max_length=12)
    specialization = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff_image = models.ImageField(upload_to='images/', null=True, blank=True)



