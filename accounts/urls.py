from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
