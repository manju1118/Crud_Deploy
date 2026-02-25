from django.shortcuts import render, redirect
from .models import Student


def home_page(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, 'home.html', context)


#student creation

def student_creation(request):
    if request.method =='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        new_student = Student.objects.create(
            first_name = fname,
            last_name = lname,
            age = age,
            email = email
        )
        new_student.save()
        return redirect('home')
    return render(request,'student_create.html')

def student_detail(request, stu_id):
    student = Student.objects.get(id=stu_id)
    return render(request, 'student_detail.html',{"student":student})



def student_update(request,stu_id):
    student = Student.objects.get(id=stu_id)
    if request.method == 'POST':
        student.first_name = request.POST.get('fname')
        student.last_name = request.POST.get('lname')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.save()
        return redirect('home')
    return render(request, 'student_update.html',{'student':student})

def student_delete(request,stu_id):
    student = Student.objects.get(id=stu_id)
    student.delete()
    return redirect('home')