from django.shortcuts import render, redirect
from myapp.models import ClassRoom, Student

# Create your views here.

def add_classroom(request):
    if request.method.lower()== "post":
        class_name= request.POST.get("classname")
        ClassRoom.objects.create(name=class_name)
        return redirect("add_classroom")
    
    classrooms= ClassRoom.objects.all()
    return render(request, template_name="forms/classroom.html", context={"classrooms":classrooms})

def add_student(request):
    students= Student.objects.all()
    return render(request, template_name="forms/add_student.html", context={"students":students})