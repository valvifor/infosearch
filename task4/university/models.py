from django.db import models


class University(models.Model):
    full_name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=15)
    create_date = models.DateField()

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    ent_year = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name
