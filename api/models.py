from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Level(models.Model):

    level_id = models.CharField(max_length = 200, primary_key=True)
    level_number = models.IntegerField(unique=True)
    answer = models.CharField(max_length=256, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.level_id} {self.level_number}"

class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.IntegerField(unique=True)
    code = models.CharField(max_length=100, null = True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    position=models.IntegerField(null=True, blank=True)
    score = models.IntegerField(default=0)
    current_level = models.ForeignKey(Level, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} {self.roll_number} {self.score}"
