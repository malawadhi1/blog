
from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now=False)

	def __str__(self):
			return self.title
