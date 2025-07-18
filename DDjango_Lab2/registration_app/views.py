from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return render(request, 'registration_app/success.html', {'student': student})
    else:
        form = StudentForm()
    return render(request, 'registration_app/register.html', {'form': form})
