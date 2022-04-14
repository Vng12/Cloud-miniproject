from django.db import models

# Create your models here.
class notice(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text