from django.shortcuts import render
from django.http import HttpResponse

from .models import Student


def home(request):
    students = Student.objects.all()

    return render(request, 'index.html', {
        'students': students
    })