from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=256)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name 

class Question(models.Model):
	url = models.URLField(null=True, blank=True)
	name = models.TextField(default="Practice")
	description = models.TextField(null=True, blank=True)
	PRIORITY_STATUS =(
			(1,'Less important'),
			(2,'Moderate Important'),
			(3,'Very Important'),
		)
	priority = models.IntegerField(choices=PRIORITY_STATUS)
	category_name = models.ForeignKey('Category')
	revise_count = models.IntegerField(default=0)
	finished = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	created = models.DateTimeField(auto_now_add=True)
	last_solved = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['priority', 'created']

	def __str__(self):
		return self.name + " " + str(self.priority)+ " "+ str(self.is_active)

class Tags(models.Model):
	name = models.CharField(max_length=256)
	referred_count = models.IntegerField(default=1)
	question = models.ManyToManyField('Question')
	is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ['-referred_count']

	def __str__(self):		
		return self.name

