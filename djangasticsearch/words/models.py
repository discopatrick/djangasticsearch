from django.db import models

class Word(models.Model):
	word_string = models.TextField()

	def __str__(self):
		return self.word_string
