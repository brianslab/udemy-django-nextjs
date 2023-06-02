from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('jobs/new/', views.newJob, name='newJob'),
    path('jobs/<str:pk>/', views.getJob, name='job'),
    path('jobs/<str:pk>/edit', views.editJob, name='editJob'),
    path('jobs/<str:pk>/delete', views.deleteJob, name='deleteJob'),
    path('jobs/<str:pk>/apply', views.applyToJob, name='applyToJob'),
    path('jobs/<str:pk>/check', views.isApplied, name='isApplied'),
    path('jobs/<str:pk>/candidates', views.getCandidatesApplied,
         name='getCandidatesApplied'),
    path('stats/<str:topic>/', views.getTopicStats, name='getTopicStats'),
    path('me/jobs/applied', views.getCurrentUserAppliedJobs,
         name='getCurrentUserAppliedJobs'),
    path('me/jobs', views.getCurrentUserCreatedJobs,
         name='getCurrentUserCreatedJobs'),
]
