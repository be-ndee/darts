from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

from django.utils.translation import ugettext_lazy as _

# Create your views here.
def welcome(request):
	template = loader.get_template('home/welcome.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


def help(request):
	template = loader.get_template('home/help.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
