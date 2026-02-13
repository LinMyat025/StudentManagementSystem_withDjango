from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Student

# Create your views here.

def home(request):
    students = Student.objects.all().order_by('id')
    students_dict = {'students': students}
    return render (request, 'home.html', students_dict)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        new_student = Student(
            name = name,
            email=email,
            gender = gender,
            phone = phone
        )
        new_student.save()
        return redirect('/')
    return render(request,'create.html')

def edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.gender = request.POST.get('gender')
        student.phone = request.POST.get('phone')
        student.save()
        return redirect('/')
    student_dict = {'student': student}
    return render(request, 'edit.html', student_dict)

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

