from django import forms
from university.models import University


class UniversityForm(forms.Form):
    full_name = forms.CharField()
    short_name = forms.CharField()
    create_date = forms.DateField()


class StudentForm(forms.Form):
    full_name = forms.CharField()
    birth_date = forms.DateField()
    university = forms.ModelChoiceField(queryset=University.objects.all().values_list('full_name', flat=True))
    ent_year = forms.IntegerField()

