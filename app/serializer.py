from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','firstname','lastname','email']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','teacher','firstname','lastname','email']
        