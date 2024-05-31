"""
URL configuration for djexample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from university.views.index_view import IndexView
from university.views.add_student_view import AddStudentView
from university.views.delete_student_view import DeleteStudentView
from university.views.edit_student_view import EditStudentView
from university.views.methods_for_requests import add_student, delete_student, edit_student


urlpatterns = [
    path('', IndexView.as_view()),
    path('add_student/', AddStudentView.as_view(), name='add_student'),
    path('add_student_submit/', add_student.submit_form, name='add_student_submit'),
    path('delete_student/', DeleteStudentView.as_view(), name='delete_student'),
    path('delete_student_submit/', delete_student.submit_form, name='delete_student_submit'),
    path('edit_student/', EditStudentView.as_view(), name='edit_student'),
    path('edit_student_submit/', edit_student.submit_form, name='edit_student_submit'),
    path('admin/', admin.site.urls),
]
