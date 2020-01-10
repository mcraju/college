from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TestSerializers,StudentApplicationSerializers,StaffSerializers
from .models import StudentApplication
from .models import Student,Staff
from django.http import Http404


class TestView(APIView):
    def get(self,request,format=None):
        return Response({"message":"get method is working"})
    def post(self,request,format=None):
        seriliazer =TestSerializers(data=request.data)

        if seriliazer.is_valid():
            return Response(seriliazer.validated_data)
        return Response(seriliazer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = StudentApplication(user)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentApplication(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffView(APIView):
    def get(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = StaffSerializers(user)
        return Response(serializer.data)

    def post(self,request):
        serializer = StaffSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
