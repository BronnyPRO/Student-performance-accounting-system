from django.views.generic.base import TemplateView


class DeleteStudentView(TemplateView):
    template_name = "delete_student.html"

    def get_context_data(self, **kwargs):
        context = super(DeleteStudentView, self).get_context_data(**kwargs)

        return
    