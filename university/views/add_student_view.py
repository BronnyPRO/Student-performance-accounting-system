from django.shortcuts import render

from collections import defaultdict

from django.views.generic.base import TemplateView

from university.models import Scores


class AddStudentView(TemplateView):
    template_name = "add_student.html"

    def get_context_data(self, **kwargs):
        context = super(AddStudentView, self).get_context_data(**kwargs)

        return
