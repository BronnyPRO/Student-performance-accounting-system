from django.views.generic.base import TemplateView


class AddSubjectView(TemplateView):
    template_name = "subjects/add_subject.html"
