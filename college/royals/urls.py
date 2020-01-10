from rest_framework.urlpatterns import format_suffix_patterns
from .api import TestView,StudentView,StaffView
from django.urls import path
from . import views

app_name = 'royals'
urlpatterns =[
    path('', views.index, name='index'),
    path('application', views.application, name='application'),
    path('stu_registration', views.student_registration, name='stu-register'),
    path('staff_register', views.staff_registration, name='staff-register'),
    path('student_login', views.student_login, name='student_login'),
    path('staff_login', views.staff_login, name='staff_login'),
    path('student_details', views.student_details, name='student_details'),
    path('staff_details', views.staff_details, name='staff_details'),
    path('test/', TestView.as_view()),
    path('student/', StudentView.as_view()),
    path('staff/', StaffView.as_view()),
    path('student/<int:pk>/', StudentView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)