from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

from user_management.models import PlayerProfile

from django.utils.translation import ugettext_lazy as _

# Create your views here.
@login_required
def index(request):
	try:
		if request.GET:
			sort_by = request.GET['sort_by']
			order = request.GET['order']
		if order == 'ASC':
			order = ''
		else:
			order = '-'
		order_by = order + sort_by
		ranking = PlayerProfile.objects.all().order_by(order_by)
	except Exception:
		ranking = PlayerProfile.objects.all().order_by('-total_score')
	template = loader.get_template('ranking/index.html')
	context = RequestContext(request, {
		'ranking': ranking
	})
	return HttpResponse(template.render(context))

