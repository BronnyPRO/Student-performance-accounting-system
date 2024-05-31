from django.views.generic.base import TemplateView


class DeleteScoreView(TemplateView):
    template_name = "scores/delete_score.html"
