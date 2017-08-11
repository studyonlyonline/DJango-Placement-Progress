from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views.generic import View

from .forms import TodoForm
from .models import *

class TodoClassView(View):
	form_class = TodoForm
	template_name = 'todo/index.html'
	
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		question_obj = Question.objects.all().order_by('category_name')
		tags_object = Tags.objects.all()
		# print question_obj
		context = {
			'form': form,
			'questions':question_obj,
			'tags':tags_object
		}	
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		context = {
			'form': form
		}
		print "here"

		if form.is_valid():
			print "form valid"
			category_object,category_created = Category.objects.get_or_create(
																name=form.cleaned_data['category'],
																is_active=True
															)
			print "category_object ", category_object
			print "created ", category_created
			question_obj = Question.objects.create(
												category_name=category_object,
												url=form.cleaned_data['url'],
												name=form.cleaned_data['name'],
												description=form.cleaned_data['description'],
												priority=form.cleaned_data['priority'],
												revise_count=form.cleaned_data['revise_count'],
												finished=form.cleaned_data['finished'],
												is_active=True
											)

			print "question object ", question_obj

			tags = form.cleaned_data['tags'].split()
			print tags
			for tag in tags:
				tag_obj, tag_created = Tags.objects.get_or_create(
																name=tag,
																is_active=True
															)
				if tag_created:
					tag_obj.question.add(question_obj)
					tag_obj.save()
				else:
					tag_obj.referred_count+=1
					tag_obj.question.add(question_obj)
					tag_obj.save() 
		else:
			print "errors ", form.errors
		return redirect('TodoClassView')

	

class TestingClassView(View):

	def get(self, request, *args, **kwargs):
		print "in get"
		return HttpResponse("get")

	def post(self, request, *args, **kwargs):
		print "in post"
		return HttpResponse("post")

	def put(self, request, *args, **kwargs):
		print "in update"
		return HttpResponse("put")	

