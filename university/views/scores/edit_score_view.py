from django.views.generic.base import TemplateView
from django import forms

from university.models import Students


class EditScoreView(TemplateView):
    template_name = "scores/edit_score.html"
