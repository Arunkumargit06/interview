from django.urls import path

from . import views

urlpatterns = [
    path('schedule', views.InterviewSchedule.as_view(), name='index'),
]
