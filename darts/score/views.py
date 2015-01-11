from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

from score.models import Throw, Score
from user_management.models import PlayerProfile
from django.core.exceptions import ObjectDoesNotExist

from django.utils.translation import ugettext_lazy as _

from common import utils

# Create your views here.
@login_required
def index(request):
	user = request.user
	player = PlayerProfile.objects.get(user=user)
	template = loader.get_template('score/index.html')
	context = RequestContext(request, {
		'player': player,
	})
	return HttpResponse(template.render(context))


@login_required
def basic_scoring(request):
	user = request.user
	player = PlayerProfile.objects.get(user=user)
	scores = Score.objects.filter(player=player)
	template = loader.get_template('score/basic_scoring.html')
	context = RequestContext(request, {
		'player': player,
		'scores': scores,
	})
	return HttpResponse(template.render(context))


@login_required
def add_points(request):
	if request.POST:
		try:
			player_profile = PlayerProfile.objects.get(user=request.user)
		except ObjectDoesNotExist:
			player_profile = PlayerProfile()
			player_profile.user = request.user
			player_profile.save()
		points = request.POST['points']
		darts_amount = request.POST['darts_amount']
		try:
			throw = Throw.objects.get(points=points, darts_amount=darts_amount)
		except ObjectDoesNotExist:
			throw = Throw()
			throw.points = points
			throw.darts_amount = darts_amount
			throw.save()
		score = Score()
		score.throw = throw
		score.player = player_profile
		score.save()
		player_profile.total_score += int(points)
		player_profile.total_darts_amount += int(darts_amount)
		player_profile.save()
		
	return redirect(utils.get_next_page(request))
