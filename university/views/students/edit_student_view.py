from django.views.generic.base import TemplateView


class EditStudentView(TemplateView):
    template_name = "students/edit_student.html"
