from django.db import models

# Create your models here.
class Teacher(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.firstname

class Student(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    
    def __str__(self):
        return self.firstname