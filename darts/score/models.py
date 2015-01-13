from django.db import models
import user_management

# Create your models here.
class Throw(models.Model):
	points = models.PositiveIntegerField(default=0, null=False)
	darts_amount = models.PositiveIntegerField(default=1, null=False)


class Score(models.Model):
	player = models.ForeignKey(user_management.models.PlayerProfile)
	throw = models.ForeignKey(Throw)
	date = models.DateTimeField(auto_now_add=True)