from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template.response import TemplateResponse
from university import models
from university.forms import StudentForm
from university.models import University, Student


def universities(request):
    university = models.University.objects.all()
    data = {"universities": university}
    return TemplateResponse(request, "universities.html", data)


def create_university(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        short_name = request.POST.get("short_name")
        create_date = request.POST.get("create_date")
        university = models.University.objects.create(full_name=full_name, short_name=short_name, create_date=create_date)
        university.save()
    return HttpResponseRedirect('/app/univ/')


def delete_university(request, id):
    try:
        university = University.objects.get(id=id)
        university.delete()
        return HttpResponseRedirect('/app/univ/')
    except University.DoesNotExist:
        return HttpResponseNotFound("<h2>Information not found</h2>")


def update_university(request, id):
    try:
        university = University.objects.get(id=id)
        if request.method == "POST":
            university.full_name = request.POST.get("full_name")
            university.short_name = request.POST.get("short_name")
            university.create_date = request.POST.get("create_date")
            university.save()
            return HttpResponseRedirect('/app/univ/')
        else:
            data = {"university": university}
            return TemplateResponse(request, "update_university.html", data)
    except University.DoesNotExist:
        return HttpResponseNotFound("<h2>Information not found</h2>")


def students(request):
    student = models.Student.objects.all()
    data = {"students": student, "form": StudentForm()}
    return TemplateResponse(request, "students.html", data)


def create_student(request):
    if request.method == "POST":
        full_name_st = request.POST.get("full_name")
        birth_date = request.POST.get("birth_date")
        university = request.POST.get("university")
        university1 = University.objects.get(full_name=university)
        ent_year = request.POST.get("ent_year")
        student = models.Student.objects.create(full_name=full_name_st, birth_date=birth_date, university=university1, ent_year=ent_year)
        student.save()
    return HttpResponseRedirect('/app/stud/')


def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect('/app/stud/')
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Information not found</h2>")


def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
        if request.method == "POST":
            student.full_name = request.POST.get("full_name")
            student.birth_date = request.POST.get("birth_date")
            student.university = request.POST.get("university")
            student.ent_year = request.POST.get("ent_year")
            student.save()
            return HttpResponseRedirect('/app/stud/')
        else:
            data = {"student": student, "form": StudentForm()}
            return TemplateResponse(request, "update_student.html", data)
    except University.DoesNotExist:
        return HttpResponseNotFound("<h2>Information not found</h2>")
