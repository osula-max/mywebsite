from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from projects.models import Project
from django.core.mail import send_mail


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

from django.shortcuts import render, redirect
from projects.forms import ContactForm
from django.http import HttpResponse



def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['andrewosula@gmail.com'], # To Email
        )
        return render(request, 'contact.html', {'message_name':message_name})
    else:
        return render(request, 'contact.html', {})



def cv(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'cv.html', context)  

def works(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'works.html', context)   









