from django.views.generic.base import TemplateView


class EditStudentView(TemplateView):
    template_name = "edit_student.html"

    def get_context_data(self, **kwargs):
        context = super(EditStudentView, self).get_context_data(**kwargs)

        return
