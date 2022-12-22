from django.contrib import admin
from university.models import Student, University


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date', 'university', 'ent_date')


admin.site.register(Student)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'short_name', 'create_date')


admin.site.register(University)
