
from django.shortcuts import redirect

from university.models import Students, Scores, Subjects


def submit_form(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        group = request.POST.get('group')

        surname_new = request.POST.get('surname_new')
        name_new = request.POST.get('name_new')
        patronymic_new = request.POST.get('patronymic_new')
        group_new = request.POST.get('group_new')

        student = (Students.objects.filter(
            surname=surname,
            name=name,
            patronymic=patronymic,
            group=group
            ).update(
                surname=surname_new,
                name=name_new,
                patronymic=patronymic_new,
                group=group_new
                )
        )

    return redirect('/')
