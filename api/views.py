from django.shortcuts import render
from rest_framework.response import Response
from api.models import *
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from datetime import datetime
import pytz

# Create your views here.

class HomeView(TemplateView):

    template_name = 'api/home.html'

class LevelView(LoginRequiredMixin, TemplateView):

    template_name = 'api/level.html'

    def get_context_data(self, **kwargs):

        context = super(LevelView, self).get_context_data(**kwargs)
        student = Student.objects.get(user=self.request.user)
        level = student.current_level
        context['level'] = level
        context['student'] = student

        return context

    def post(self, request):

        student = Student.objects.get(user=request.user)
        level = student.current_level
        if request.POST['answer'].casefold() == level.answer.casefold():
            if(datetime.now()<datetime(2021, 2, 20, 16, 0, 0, 0)):
                student.score+=level.score
                student.time_stamp = datetime.now()
            try:
                student.current_level = Level.objects.get(level_number = level.level_number+1)
            except Level.DoesNotExist:
                student.finish=1
            print(student.current_level)
            print(student.score)
            student.save()

        return HttpResponseRedirect("/level")

class LeaderboardView(TemplateView):

    template_name="api/leaderboard.html"

    def get_context_data(self, **kwargs):

        context = super(LeaderboardView, self).get_context_data(**kwargs)
        students = list(Student.objects.all().order_by('-score', 'time_stamp'))
        position = 1
        for i in range(len(students)):
            students[i].position=i+1
            students[i].save()

        context['students']=students

        return context

class RegistrationAPI(APIView):

    def get(self, request):

        username = request.GET.get('username');
        try:
            User.objects.get(username=username)
            return JsonResponse(status=200, data={"message":"error"})
        except User.DoesNotExist:
            return JsonResponse(status=200, data={"message":"gg"})


    def post(self, request):
        data = json.loads(request.body)
        print(data)
        otpcode = data['code']
        rollno = data['rollno']
        first_name = data['firstname']
        last_name = data['lastname']
        email = data['email']
        username = data['username']
        password = data['password']

        c = code(username)
        if c!=otpcode:
            return JsonResponse(status=400, data={"message":"code invalid"})

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        student = Student(user=user, roll_number=rollno, code=otpcode, current_level=Level.objects.get(level_number=1))
        student.save()
        return JsonResponse(status=200, data={"message":"successfull"})


def code(username):

    sum=0
    for i in username:
        sum+=ord(i)
    a = 2310433
    c = 2342201
    m = 2147483648
    x = (a * sum + c) % m
    return x

