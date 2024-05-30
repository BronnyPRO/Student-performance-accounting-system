from django.contrib import admin

from university.models import Students
from django.contrib import admin


admin.site.register(Students, admin.ModelAdmin)
