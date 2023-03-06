from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('job_seeker/register/', views.job_seeker_register, name='job_seeker_register'),
    path('employer/register/', views.employer_register, name='employer_register'),
    path('job_seeker/login/', views.job_seeker_login, name='job_seeker_login'),
    path('employer/login/', views.employer_login, name='employer_login'),
    path('job_seeker/dashboard/', views.job_seeker_dashboard, name='job_seeker_dashboard'),
    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('job_seeker/logout/', views.job_seeker_logout, name='job_seeker_logout'),
    path('employer/logout/', views.employer_logout, name='employer_logout'),
]