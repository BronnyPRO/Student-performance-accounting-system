from django.views.generic.base import TemplateView


class DeleteSubjectView(TemplateView):
    template_name = "subjects/delete_subject.html"
