from django.contrib import admin
from .models import StudentApplication, Student, Staff, Department

admin.site.register(StudentApplication)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Staff)



