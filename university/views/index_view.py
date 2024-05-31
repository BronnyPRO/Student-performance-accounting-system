from collections import defaultdict

from statistics import mean

from django.views.generic.base import TemplateView

from university.models import Subjects, Scores


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        scores = Scores.objects.all()
        student_scores = defaultdict(dict)

        subjects = set()
        for score in scores:
            subject_name = score.subject.name
            subjects.add(subject_name)
            student_scores[score.student][subject_name] = score.value

        subjects = sorted(subjects)
        student_statistics = [
            {
                'student': student,
                'scores': [f'{scores[subject]:.1f}' for subject in subjects],
                'average_score': f'{mean([scores[subject] for subject in subjects]):.1f}'
            }
            for student, scores in student_scores.items()
        ]

        average_scores = [
            {
                'subject': subject,
                'average_score': f'{mean([scores[subject] for _, scores in student_scores.items()]):.1f}'
            }
            for subject in subjects
        ]

        best_student = student_statistics[0]['student']
        average_score = float(student_statistics[0]['average_score'])
        for student in student_statistics[1:]:
            if float(student['average_score']) > average_score:
                best_student = student['student']
                average_score = float(student['average_score'])

        worse_student = student_statistics[0]['student']
        average_score = float(student_statistics[0]['average_score'])
        for student in student_statistics[1:]:
            if float(student['average_score']) < average_score:
                worse_student = student['student']
                average_score = float(student['average_score'])

        context.update(
            {
                'subjects': subjects,
                'student_statistics': student_statistics,
                'average_scores': average_scores,
                'best_student': best_student,
                'worse_student': worse_student
            }
        )
        return context
