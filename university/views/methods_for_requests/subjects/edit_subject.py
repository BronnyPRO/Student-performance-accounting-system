
from django.shortcuts import redirect

from university.models import Subjects


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        name_new = request.POST.get('name_new')

        Subjects.objects.filter(name=name).update(name=name_new)

    return redirect('/')
