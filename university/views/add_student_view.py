from django.views.generic.base import TemplateView


class AddStudentView(TemplateView):
    template_name = "add_student.html"
