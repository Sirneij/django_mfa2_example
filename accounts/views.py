from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.utils import timezone
from django.http import HttpResponseBadRequest
from .models import User

from . import utils

def login(request):
    context = {
        'page_title': "Login",
    }
    return render(request, 'login.html', context)

def register(request):
    error = ''
    if request.method == "POST":
        username = request.POST.get('username')
        display_name = request.POST.get('display-name')
        #if not utils.validate_username(username):
        #    error = 'Invalid matriculation number'
         #   return HttpResponseBadRequest('Invalid matriculation number')
        #elif not utils.validate_display_name(display_name):
        #    error = 'Invalid display name'
         #   return HttpResponseBadRequest('Invalid display name')

        if User.objects.filter(username=username).exists():
            error = 'Student already exists.'
            return HttpResponseBadRequest('Student already exists.')
        else:
            u = User.objects.create(first_name = display_name, password='none', is_superuser=False, username=username,  last_name='', display_name=display_name, email='none', is_staff=False, is_active=True,date_joined=timezone.now())
            u.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login(request,u)
            return redirect(reverse('start_fido2'))

    context = {
        'page_title': "Register",
        'error': error
    }
    return render(request, 'register.html', context)
