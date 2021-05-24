from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
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
        if not utils.validate_username(username):
            error = 'Invalid matriculation number'
            return HttpResponseBadRequest('Invalid matriculation number')
        elif not utils.validate_display_name(display_name):
            error = 'Invalid display name'
            return HttpResponseBadRequest('Invalid display name')

        elif User.objects.filter(username=username).first():
            error = 'Student already exists.'
            return HttpResponseBadRequest('Student already exists.')
        else:
            User.objects.create(password='none', is_superuser=False, username=username, first_name='none',  last_name='none', display_name=display_name, email='none', is_staff=False, is_active=True,date_joined=timezone.now())
            authenticate(username=username, display_name=display_name)
            return redirect(reverse('fido2_begin_reg'))

    context = {
        'page_title': "Register",
        'error': error
    }
    return render(request, 'register.html', context)
