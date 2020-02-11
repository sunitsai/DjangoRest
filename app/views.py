from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import viewsets
# Create your views here.

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class =  TeacherSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer