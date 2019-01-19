from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
import bcrypt


# Create your views here.
def index(request):

    return render(request, 'handy/index.html')

def register(request):
    errors = User.objects.validation(request.POST)
    if 'errors' in errors:
        for key, value in errors['errors'].items():
            messages.error(request, value)
        return redirect('/')
    else:
        request.session['first_name'] = User.objects.get(email=request.POST['email']).first_name
        request.session['id'] = User.objects.get(email=request.POST['email']).id
        return redirect('/dashboard')

def signin(request):
    errors = User.objects.login_validation(request.POST)
    if 'errors' in errors:
        for key, value in errors['errors'].items():
            messages.error(request, value)
        return redirect('/')
    else: 
        request.session['first_name'] = User.objects.get(email=request.POST['email']).first_name
        request.session['id'] = User.objects.get(email=request.POST['email']).id
        return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    u = User.objects.get(id=request.session['id'])
    context = {
        'jobs': Job.objects.exclude(user_joblist=u),
        'myjobs': Job.objects.filter(user_joblist=u)
    }
    return render(request, 'handy/dashboard.html', context)

def addjob(request):

    return render(request, 'handy/addjob.html')

def process_new_job(request):
    users = User.objects.get(id=request.session['id'])
    if len(request.POST['jobtitle'])<3:
        messages.error(request, 'Title must be 3 characters long.')
        return redirect('/addjob')
    if len(request.POST['description'])<10:
        messages.error(request, 'Description must be 10 characters long.')
        return redirect('/addjob')
    if len(request.POST['location'])<1:
        messages.error(request, 'Location must be present.')
        return redirect('/addjob')
    else:
        Job.objects.create(name=request.POST['jobtitle'], description=request.POST['description'], location=request.POST['location'], addedby=users)
    return redirect('/dashboard')

def add_job_to_list(request, job_id):
    u = User.objects.get(id=request.session['id'])
    j = Job.objects.get(id=job_id)
    u.joblist.add(j)
    u.save()
    return redirect('/dashboard')

def remove_job_from_list(request, job_id):
    j = Job.objects.get(id=job_id)
    j.joblist.remove(request.session['id'])
    j.save()
    return redirect('/dashboard')

def job_list(request, job_id):
    j = Job.objects.get(id=job_id)
    p = j.user_joblist.all()
    context = {
        'myjobs': p,
        'myjob': j
    }
    return redirect(request, '/dashboard', context)

def job_detail(request, job_id):
    context = {
        'job': Job.objects.get(id=job_id)
    }
    return render(request, 'handy/view.html', context)

def edit(request, job_id):
    context = {
        'job': Job.objects.get(id=job_id)
    }
    return render(request, 'handy/edit.html', context)

# def edit_job(request, job_id):
#     if request.method == "POST":
#         j = Job.objects.get(id=job_id)
#         j.id = job_id
#         j.name = request.POST['name']
#         j.description = request.POST['description']
#         j.location = request.POST['location']
#         return redirect(request, '/dashboard')
#     else:
#         return redirect(request, '/dashboard')

def delete(request, job_id):
    Job.objects.get(id=job_id).delete()
    return redirect('/dashboard')