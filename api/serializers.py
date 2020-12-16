from rest_framework import serializers
from api.models import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'email',)

class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:

        model = Participant
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Level
        fields = '__all__'
