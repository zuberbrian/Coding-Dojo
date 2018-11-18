from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'courses' : Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def process(request):
    result = Course.objects.validation(request.POST)
    if 'errors' in result :
        for key, value in result['errors'].items():
            messages.error(request, value)
    return redirect('/')

def destroy(request, number):
    context = {
        'course' : Course.objects.get(id=number)
    }
    return render(request, 'courses/destroy.html', context)

def confirm(request, number):
    Course.objects.get(id=number).delete()
    return redirect('/')