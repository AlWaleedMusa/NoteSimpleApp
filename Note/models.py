from django.db import models

# Create your models here.
class Notes(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=50, blank=True)
	body = models.TextField(max_length=1000)

	def __str__(self):
		return "{}".format(self.title)