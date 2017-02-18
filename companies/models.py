from django.db import models

class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	open_price = models.FloatField()
	close_price = models.FloatField()
	volume = models.IntegerField()

	def __str__(self):
		return self.ticker
		
