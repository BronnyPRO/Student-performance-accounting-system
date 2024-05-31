from django.shortcuts import redirect

from university.models import Subjects


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        Subjects.objects.filter(name=name).delete()

    return redirect('/')
