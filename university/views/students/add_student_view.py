from django.views.generic.base import TemplateView


class AddStudentView(TemplateView):
    template_name = "students/add_student.html"
