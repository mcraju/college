from django.shortcuts import render
from .models import StudentApplication, Department, Student, Staff
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def index(request):
    return render(request, 'royals/index.html')


def application(request):
    if request.method == 'POST':
        StudentApplication.objects.create(
            student_name = request.POST['student_name'],
            email = request.POST['email'],
            ssc_percentage = request.POST['ssc_percentage'],
            inter_percentage = request.POST['inter_percentage'])
        return HttpResponseRedirect('/royals/')
    return render(request, 'royals/application.html')


def student_registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        student = StudentApplication.objects.get(email=email, is_verified=True)
        user= User.objects.create_user(
            username= request.POST['username'],
            password= request.POST['password'],
            email= request.POST['email']
        )
        department = Department.objects.get(department_name =request.POST['department'])
        if student.email == user.email:
            Student.objects.create(
                student_name= request.POST['student_name'],
                dob= request.POST['dob'],
                father_name= request.POST['father_name'],
                mother_name= request.POST['mother_name'],
                mobile_no= request.POST['mobile_no'],
                gender= request.POST['gender'],
                student_image= request.FILES['student_image'],
                student_application=student,
                department=department,
                user=user
            )
            return HttpResponseRedirect('/royals/')
    return render(request, 'royals/student_registration.html')


def staff_registration(request):
    if request.method == 'POST':
        user=User.objects.create_user(
            username= request.POST['username'],
            password= request.POST['password'],
            email= request.POST['email']
        )
        department = Department.objects.get(department_name= request.POST['department'])
        Staff.objects.create(
            staff_name= request.POST['staff_name'],
            mobile_no = request.POST['mobile_no'],
            experience= request.POST['experience'],
            specialization= request.POST['specialization'],
            gender= request.POST['gender'],
            department= department,
            user=user
        )
        return HttpResponseRedirect('/royals/')
    return render(request, 'royals/staff_register.html')


def student_login(request):
    if request.method=='POST':
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/royals/student_details/')
        else:
            return render(request, 'royals/student_login.html', {'error_message': 'Invalid Credentials'})
    return render(request, 'royals/student_login.html')


def staff_login(request):
    if request.method=='POST':
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/royals/staff_details')
        else:
            return render(request, 'royals/staff_login.html', {'error_message': 'Invalid Credentials'})
    return render(request, 'royals/staff_login.html')


def student_details(request):
    student = request.user.student
    return render(request, 'royals/student_details.html', {'student':student})


def staff_details(request):
    staff = request.user.staff
    return render(request, 'royals/staff_details.html', {'staff': staff})