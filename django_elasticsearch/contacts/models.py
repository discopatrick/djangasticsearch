from django.db import models

class Contact(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)
