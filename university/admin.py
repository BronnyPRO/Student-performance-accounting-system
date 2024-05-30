from django.contrib import admin

from university.models import Students, Subjects, Scores
from django.contrib import admin


admin.site.register(Students, admin.ModelAdmin)
admin.site.register(Subjects, admin.ModelAdmin)
admin.site.register(Scores, admin.ModelAdmin)
