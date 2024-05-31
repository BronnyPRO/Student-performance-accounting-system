from django.views.generic.base import TemplateView


class DeleteStudentView(TemplateView):
    template_name = "students/delete_student.html"
    