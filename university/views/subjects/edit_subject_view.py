from django.views.generic.base import TemplateView


class EditSubjectView(TemplateView):
    template_name = "subjects/edit_subject.html"
