from django.shortcuts import redirect

from university.models import Students, Scores, Subjects


def submit_form(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        group = request.POST.get('group')

        Students.objects.filter(surname=surname, name=name, patronymic=patronymic, group=group).delete()

    return redirect('/')
