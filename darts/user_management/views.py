from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate as django_authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.core.mail import send_mail

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

from user_management.models import PlayerProfile

from common import utils
import re


# Create your views here.
def login(request):
    if not request.POST:
        template = loader.get_template('user_management/login.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))
    username = request.POST['username']
    password = request.POST['password']
    user = django_authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            django_login(request, user)
            # Redirect to a success page.
            return redirect(utils.get_next_page(request))
        else:
            # Return a 'not active account' error message
            return redirect(utils.get_next_page(request))
    # Return an 'invalid login' error message.
    return redirect(utils.get_next_page(request))


def logout(request):
    django_logout(request)
    return redirect(utils.get_next_page(request))


def register(request):
    template = loader.get_template('user_management/register.html')
    if not request.POST or request.user.is_authenticated():
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))
    
    # create error array
    errors = {}
    # check if user exists
    username = request.POST['username']
    try:
        user = User.objects.get(username=username)
        errors['username'] = _('The username already exists.')
    except ObjectDoesNotExist:
        user = User()

    # validate username
    USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9_@+.-]{4,30}$')
    if not USERNAME_REGEX.match(username):
        errors['username'] = _('The username is not correct.')

    # validate email
    email = request.POST['email']
    EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]')
    if not EMAIL_REGEX.match(email):
        errors['email'] = _('The email is not valid.')

    # validate password
    password = request.POST['password']
    password_repeat = request.POST['password_repeat']
    PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9_@+.-]{4,30}$')
    if password != password_repeat or not PASSWORD_REGEX.match(password):
        errors['password'] = _('The passwords do not match.')
    
    # if errors created, return them
    if len(errors) > 0:
        context = RequestContext(request, {
            'errors': errors,
            'email': email,
            'username': username,
        })
        return HttpResponse(template.render(context))
    # save data
    user.username = username
    user.set_password(password)
    user.email = email
    # TODO email user
    user.save()
    # create profile
    profile = PlayerProfile()
    profile.user = user
    profile.save()

    template = loader.get_template('user_management/register_success.html')
    context = RequestContext(request, {
        'username': user.username
    })
    return HttpResponse(template.render(context))
