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

from university.views.students.add_student_view import AddStudentView
from university.views.students.delete_student_view import DeleteStudentView
from university.views.students.edit_student_view import EditStudentView

from university.views.subjects.add_subject_view import AddSubjectView
from university.views.subjects.delete_subject_view import DeleteSubjectView
from university.views.subjects.edit_subject_view import EditSubjectView

from university.views.scores.edit_score_view import EditScoreView
from university.views.scores.delete_score_view import DeleteScoreView

from university.views.methods_for_requests.students import add_student, edit_student, delete_student
from university.views.methods_for_requests.subjects import edit_subject, add_subject, delete_subject
from university.views.methods_for_requests.scores import edit_score, delete_score

urlpatterns = [
    path('', IndexView.as_view()),
    path('add_student/', AddStudentView.as_view(), name='add_student'),
    path('add_student_submit/', add_student.submit_form, name='add_student_submit'),
    path('delete_student/', DeleteStudentView.as_view(), name='delete_student'),
    path('delete_student_submit/', delete_student.submit_form, name='delete_student_submit'),
    path('edit_student/', EditStudentView.as_view(), name='edit_student'),
    path('edit_student_submit/', edit_student.submit_form, name='edit_student_submit'),

    path('add_subject/', AddSubjectView.as_view(), name='add_subject'),
    path('add_subject_submit/', add_subject.submit_form, name='add_subject_submit'),
    path('delete_subject/', DeleteSubjectView.as_view(), name='delete_subject'),
    path('delete_subject_submit/', delete_subject.submit_form, name='delete_subject_submit'),
    path('edit_subject/', EditSubjectView.as_view(), name='edit_subject'),
    path('edit_subject_submit/', edit_subject.submit_form, name='edit_subject_submit'),

    path('edit_score/', EditScoreView.as_view(), name='edit_score'),
    path('edit_score_submit/', edit_score.submit_form, name='edit_score_submit'),
    path('delete_score/', DeleteScoreView.as_view(), name='delete_score'),
    path('delete_score_submit/', delete_score.submit_form, name='delete_score_submit'),

    path('admin/', admin.site.urls),
]
