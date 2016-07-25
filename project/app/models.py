from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
	id=models.AutoField
	name=models.CharField(max_length=50)
	surname=models.CharField(max_length=50)
	othernames=models.CharField(max_length=50)
	email=models.EmailField(max_length=100)

	class Meta:
		db_table="Users"
		verbose_name_plural="Users"
	def __str__(self):
		return u"%s %s %s %s %s" %(self.id, self.name, self.surname, self.othernames, self.email)


class Post(models.Model):
	# author=models.ForeignKey(name.Users)
	title=models.CharField(max_length=100)
	text=models.TextField()
	Created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)

	def published(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
