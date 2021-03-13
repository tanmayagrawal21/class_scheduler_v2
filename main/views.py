from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.
def index(request):
    return render(request, "main/index.html",{
        "students": Student.objects.all(),
        "six": Student.objects.filter(std=6),
        "seven": Student.objects.filter(std=7),
        "eight": Student.objects.filter(std=8),
        "nine": Student.objects.filter(std=9),
        "ten": Student.objects.filter(std=10),
            })
def teacher(request):
    return HttpResponse("This will be the teachers' database")

def student(request, id):
    student= Student.objects.get(id=id)
    return HttpResponse(f"<h1>{student}</h1>")

def create(request):
    print(request.POST)
    if request.method=="POST":
        if request.POST.get("submit"):
            for student in Student.objects.all():
                if request.POST.get("c"+str(student.id))=="selected":
                    student.num_absent+=1
                    student.save()
            return redirect(index)

    return render(request, "main/create.html",{
        "students": Student.objects.all(),
        "six": Student.objects.filter(std=6),
        "seven": Student.objects.filter(std=7),
        "eight": Student.objects.filter(std=8),
        "nine": Student.objects.filter(std=9),
        "ten": Student.objects.filter(std=10),
            })
