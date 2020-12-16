from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.IntegerField(unique=True)
    phone_number = PhoneNumberField()

class Level(models.Model):

    level_id = models.CharField(max_length = 200, primary_key=True)
    level_number = models.IntegerField(unique=True)
    link = models.URLField()
    score = models.IntegerField()
    decay = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __init__(self):

        return level_id

class Participant(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    current_level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __init__(self):
        return roll_no
