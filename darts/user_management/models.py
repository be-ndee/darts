from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import score

# Create your models here.
class PlayerProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	total_score = models.PositiveIntegerField(default=0, null=False)
	total_darts_amount = models.PositiveIntegerField(default=0, null=False)
	one_dart_average = models.FloatField(default=0, null=False)
	three_darts_average = models.FloatField(default=0, null=False)

	def save(self):
		self.one_dart_average = self.get_one_dart_average()
		self.three_darts_average = self.get_three_darts_average()
		super(PlayerProfile, self).save()


	def get_one_dart_average(self):
		if self.total_darts_amount == 0:
			return 0
		return (self.total_score / self.total_darts_amount)


	def get_three_darts_average(self):
		return (self.get_one_dart_average() * 3)


	def throw_darts(self, points, darts_amount):
		try:
			throw = score.models.Throw.objects.get(points=points, darts_amount=darts_amount)
		except ObjectDoesNotExist:
			throw = score.models.Throw()
			throw.points = points
			throw.darts_amount = darts_amount
			throw.save()
		point_score = score.models.Score()
		point_score.throw = throw
		point_score.player = self
		point_score.save()
		self.total_score += points
		self.total_darts_amount += darts_amount
		self.save()
