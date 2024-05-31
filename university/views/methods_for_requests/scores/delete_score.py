from django.shortcuts import redirect

from university.models import Students, Subjects, Scores


def submit_form(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        group = request.POST.get('group')

        subject_name = request.POST.get('subject')

        student = Students.objects.filter(surname=surname, name=name, patronymic=patronymic, group=group)[0]
        subject = Subjects.objects.filter(name=subject_name)[0]

        Scores.objects.filter(student=student, subject=subject).update(value=0)

    return redirect('/')
