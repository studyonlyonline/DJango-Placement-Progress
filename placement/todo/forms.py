from django.forms import ModelForm
from .models import Question

class TodoForm(ModelForm):

	# error_css_class = 'error'
    # required_css_class = 'required'
    class Meta:
		model = Question
		fields = [ 'category_name', 'name', 'url', 'description', 'priority', 'revise_count', 'finished']

	# category = forms.CharField(label="category")
	# name = forms.CharField(label="Name")
	# url = forms.URLField(label="URL")
	# description = forms.CharField(label="Description")