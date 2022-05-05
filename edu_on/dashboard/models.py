from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    status = models.BooleanField(default=False)


class Course(models.Model):
    name = models.CharField(max_length=256)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.IntegerField()








