from django import forms
# from django.forms import ModelForm
from .models import Question

class TodoForm(forms.Form):

	error_css_class = 'error'
    # required_css_class = 'required'
  #   class Meta:
		# model = Question
		# fields = [ 'category_name', 'name', 'url', 'description', 'priority', 'revise_count', 'finished']

	#choices
	PRIORITY_STATUS =(
			(1,'Less important'),
			(2,'Moderate Important'),
			(3,'Very Important'),
		)

	category = forms.CharField(label="category")
	name = forms.CharField(label="Name")
	url = forms.URLField(label="URL")
	description = forms.CharField(label="Description", widget=forms.Textarea, required=False)
	tags = forms.CharField(label="Tags")
	priority = forms.ChoiceField(label = "Priority ", choices=PRIORITY_STATUS, required=True)
	revise_count= forms.IntegerField(label="Revise",initial=0)
	finished = forms.BooleanField(label="Finished", initial=False,required=False)

	

