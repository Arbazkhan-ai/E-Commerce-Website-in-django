from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student


def home(request):
    students = Student.objects.all()

    return render(request, 'index.html', {
        'students': students
    })

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = StudentForm()

    return render(request, 'add_student.html', {
        'form': form
    })
def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = StudentForm(instance=student)

    return render(request, 'Manue/edit_student.html', {
        'form': form
    })