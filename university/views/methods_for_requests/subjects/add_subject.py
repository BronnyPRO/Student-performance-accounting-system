from django.shortcuts import redirect

from university.models import Students, Scores, Subjects


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        subject = Subjects.objects.create(name=name)
        subject.save()

        students = Students.objects.all()

        for student in students:
            score = Scores.objects.create(student=student, subject=subject)
            score.save()

    return redirect('/')
