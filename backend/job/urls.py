from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('jobs/new/', views.newJob, name='newJob'),
    path('jobs/<str:pk>/', views.getJob, name='job'),
    path('jobs/<str:pk>/edit/', views.editJob, name='editJob'),
]
