from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PlayerProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	total_score = models.PositiveIntegerField(default=0, null=False)
	total_darts_amount = models.PositiveIntegerField(default=0, null=False)
	total_average = models.FloatField(default=0, null=False)

	def save(self):
		self.total_average = self.get_average()
		super(PlayerProfile, self).save()

	
	def get_average(self):
		if self.total_darts_amount == 0:
			return 0
		return (self.total_score / self.total_darts_amount)
