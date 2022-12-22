from django.urls import path
from django.urls import include

from university import views

urlpatterns = [
    path('univ/', views.universities),
    path('univ/create/', views.create_university),
    path('univ/delete/<int:id>/', views.delete_university),
    path('univ/update/<int:id>/', views.update_university),
    path('stud/', views.students),
    path('stud/create/', views.create_student),
    path('stud/delete/<int:id>/', views.delete_student),
    path('stud/update/<int:id>/', views.update_student)
]
