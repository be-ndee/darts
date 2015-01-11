from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

from django.utils.translation import ugettext_lazy as _

from common import utils

# Create your views here.
@login_required
def index(request):
	template = loader.get_template('score/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


@login_required
def basic_scoring(request):
	template = loader.get_template('score/basic_scoring.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


@login_required
def add_points(request):
	if request.POST:
		points = request.POST['points'] # e.g. 121
		darts_amount = request.POST['darts_amount'] # e.g. 3 darts
		# shots ? (e.g.: triple-20, double-12, ...)
		# save
	return redirect(utils.get_next_page(request))
