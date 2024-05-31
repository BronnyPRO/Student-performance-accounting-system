from django.shortcuts import redirect

from university.models import Students, Scores, Subjects


def submit_form(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        group = request.POST.get('group')

        student = Students.objects.create(surname=surname, name=name, patronymic=patronymic, group=group)
        student.save()

        scores = Scores.objects.all()

        subjects = Subjects.objects.all()

        for subject in subjects:
            score = Scores.objects.create(student=student, subject=subject)
            score.save()

    return redirect('/')
