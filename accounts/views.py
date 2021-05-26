from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.utils import timezone
from django.conf import settings
from .models import User
from . import utils

def login_user_in(request, username):
    user=User.objects.get(username=username)
    user.backend='django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)
    if "redirect" in request.POST:
        return redirect(request.POST["redirect"])
    else:
        return redirect(reverse('accounts:index'))

def login(request):
    if request.method == "POST":
        username = request.POST.get('username').replace('/', '')
        user = User.objects.filter(username=username).first()
        err=""
        if user is not None:
            if user.is_active:
                if "mfa" in settings.INSTALLED_APPS:
                    from mfa.helpers import has_mfa
                    res =  has_mfa(request,username=username)
                    if res: return res
                    return login_user_in(request, username)
            else:
                err="This student is NOT activated yet."
        else:
            err="No student with such matriculation number exists."
        return render(request, 'login.html', {"err":err})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        error = ''
        username = request.POST.get('username').replace('/', '')
        display_name = request.POST.get('display-name')
        if not utils.validate_username(username):
           error = 'Invalid matriculation number'
           return render(request, 'register.html', context = {'page_title': "Register", 'error': error})
        if not utils.validate_display_name(display_name):
           error = 'Invalid display name'
           return render(request, 'register.html', context = {'page_title': "Register", 'error': error})
        if User.objects.filter(username=username).exists():
            error = 'Student already exists.'
            return render(request, 'register.html', context = {'page_title': "Register", 'error': error})
        else:
            u = User.objects.create(first_name = display_name, password='none', is_superuser=False, username=username,  last_name='', display_name=display_name, email='none', is_staff=False, is_active=True,date_joined=timezone.now())
            u.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login(request,u)
            return redirect(reverse('start_fido2'))
    else:
        return render(request, 'register.html', context = {'page_title': "Register"})

def index(request):
    return render(request, 'index.html', {"page_title": "Welcome home"})