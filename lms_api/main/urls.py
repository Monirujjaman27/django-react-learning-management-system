
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('teachers/', views.TeacherList.as_view()),
    path('teachers/<int:pk>/', views.TeacherDetails.as_view()),
]
