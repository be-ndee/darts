from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
	template = loader.get_template('home/welcome.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


def help(request):
	template = loader.get_template('home/help.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))