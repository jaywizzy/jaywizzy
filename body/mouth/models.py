from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	image = models.FileField(null=True, blank=True)
	content = models.TextField()
	published_date = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	time_stamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("site:post_detail", kwargs={"id":self.id})
	class Meta:
		ordering = ["-id"]

class UserLogin(models.Model):
	username = models. CharField(max_length=100)
	password = models. CharField(max_length=100)

	def __str__(self):
		return self.username
	class Meta:
		db_table = "userlogin"