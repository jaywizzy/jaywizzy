from django.db import models
from django.utils import timezone
# Create your models here.

class	Users(models.Model):
	# 	id=	models.IntegerField(null= False, primary key)
	first_name	=	models.CharField(max_length=200)
	last_name	=	models.CharField(max_length=200)
	date_of_birth	=	models.DateField(blank=False, null=False)
	sex	=	models.CharField(max_length=200)

	def __str__ (self):
		return u'%s %s %s %s' %(self.first_name, self.last_name, self.date_of_birth, self.sex)


class	Admins(models.Model):
	# id	=	models.IntegerField(null= False, primary key)
	username	=	models.CharField(max_length=200)
	lastname	=	models.CharField(max_length=200)
	password	=	models.CharField(max_length=200)

	def __str__ (self):
		return u'%s %s %s' %(self.username, self.lastname, self.password)

class	Lagosians(models.Model):
	# id	=	models.IntegerField(null= False, primary key)
	username	=	models.CharField(max_length=200)
	lastname	=	models.CharField(max_length=200)
	password	=	models.CharField(max_length=200)
	date_of_birth	=	models.DateField(blank=False,	null=False)
	def __str__ (self):
		return u'%s %s %s %s' %(self.username, self.lastname, self.password,self.date_of_birth)

class	Lasgidi(models.Model):
	# id	=	models.IntegerField(null=False, primary key)
	username	=	models.CharField(max_length=200)
	lastname	=	models.CharField(max_length=200)
	password	=	models.CharField(max_length= 200)
	date_of_birth	=	models.DateField(blank=False,	null=False)


	def __str__ (self):
		return u'%s %s %s %s' %(self.username, self.lastname, self.password,self.date_of_birth)

class	Wizzy(models.Model):
	id	=	models.AutoField(primary_key=True)
	first_name	=	models.CharField(max_length=200)
	last_name	=	models.CharField(max_length=200)
	password	=	models.CharField(max_length=200)
	sex   = 	models.CharField(max_length= 200)
	date_of_birth	=	models.DateField(blank=False,	null=False)

	
	def __str__ (self):
		return u'%s %s %s %s %s %s' %(self.id, self.first_name, self.last_name, self.password,self.sex, self.date_of_birth)




    
