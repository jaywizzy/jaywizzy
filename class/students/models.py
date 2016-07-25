from django.db import models
from django.utils import timezone
 
# Create your models here.
class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	text=models.TextField()
	# created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title

class Music(models.Model):
	artiste=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	date_released=models.DateField(max_length=50)
	duration=models.CharField(max_length=50)

	class Meta:
		db_table='music category'
		verbose_name_plural='music category'
		ordering=['artiste']
	def __str__ (self):
		return u'%s %s %s %s' %(self.artiste, self.title, self.date_released, self.duration)

class Contact(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	message=models.CharField(max_length=250)
	email=models.EmailField(max_length=50)
	def __str__(self):
		return u'%s %s %s %s %s' %(self.id, self.name, self.subject, self.message, self.email)

class Articles(models.Model):
	# author=models.ForeignKey('name.Contact')
	article=models.TextField(max_length=1000)
	article_no=models.AutoField(primary_key=True)
	published_date=models.DateTimeField(blank=True, null=True)
	class Meta:
		db_table='Articles'
		verbose_name_plural="Articles"

	def publish(self):
		self.published_date= timezone.now()
		self.save()
		
	def __str__(self):
		return u'%s %s' %(self.article_no, self.published_date, )

