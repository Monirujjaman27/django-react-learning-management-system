from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TeacherSerializer
from . import models
class TeacherList (APIView):
    def get(self,request):
        teachers = models.Teacher.objects.all() 
        teachers = TeacherSerializer(teachers, many=True)
        return Response(teachers.data)
