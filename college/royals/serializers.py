from rest_framework import serializers
from .models import StudentApplication
from .models import Student,Staff,Department
from django.contrib.auth.models import User

class TestSerializers(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    ssc_percentage = serializers.CharField()

class StudentApplicationSerializers(serializers.Serializer):

    class Meta:
        model = StudentApplication
        fields = ["student_name","email","ssc_percentage","inter_percentage"]

        def create(self,validated_data):
            return StudentApplication.objects.create(**validated_data)



class StudentSerializer(serializers.Serializer):

    class Meta:
        model = Student
        fields =["student_application","user","student_name","dob","father_name","mother_name","mobile_no",
                 "gender","department","ssc_percentage","inter_percentage"]

        def create(self,validated_data):
            return Student.objects.create(**validated_data)


class StaffSerializers(serializers.Serializer):

    class Meta:
        model = Staff
        fields = ["user","staff_name","mobile_name","experiance","specialization","gender","department"]

        def create(self,validated_data):
            return Staff.objects.create(**validated_data)



class DepartmentSerializer(serializers.Serializer):

    class Meta:
        model = Department
        fields = ["department_name"]

