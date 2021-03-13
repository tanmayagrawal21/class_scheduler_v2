from django.urls import path
from . import views

urlpatterns= [
    path("", views.index, name= "index"),
    path("teachers/", views.teacher, name="teacher"),
    path("students/<int:id>", views.student, name= "student_info"),
    path('create/', views.create, name="create_first_form")

]