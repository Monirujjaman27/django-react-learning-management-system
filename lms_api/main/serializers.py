from rest_framework import serializers
from . import models
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.Teacher
        fields = ['id','name','email','password','phone','qualification','address']