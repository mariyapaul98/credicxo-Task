"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_student_add/', views.admin_student_add, name='admin_student_add'),
    path('admin_student_view/', views.admin_student_view, name='admin_student_view'),
    path('admin_faculty_add/', views.admin_faculty_add, name='admin_faculty_add'),
    path('admin_faculty_view/', views.admin_faculty_view, name='admin_faculty_view'),
    

    path('faculty_login/', views.faculty_login, name='faculty_login'),
    path('faculty_home/', views.faculty_home, name='faculty_home'),
    path('faculty_register/', views.faculty_register, name='faculty_register'),
    path('faculty_logout/', views.faculty_logout, name='faculty_logout'),
    path('faculty_student_add/', views.faculty_student_add, name='faculty_student_add'),
    path('faculty_student_view/', views.faculty_student_view, name='faculty_student_view'),
    
    path('student_login/', views.student_login, name='student_login'),
    path('student_home/', views.student_home, name='student_home'),
    path('student_register/', views.student_register, name='student_register'),
    path('student_logout/', views.student_logout, name='student_logout'),
    path('student_student_view/', views.student_student_view, name='student_student_view'),
    path('student_faculty_view/', views.student_faculty_view, name='student_faculty_view'),
]
