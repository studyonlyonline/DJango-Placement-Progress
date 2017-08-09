from django.shortcuts import render
from django.http import HttpResponse

from .forms import TodoForm

# Create your views here.
def testing(request):
	return HttpResponse("THis is response")

def TodoView(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
	else:
		form = TodoForm()

	context = {
		'form': form
	}
	return render(request,'todo/index.html',context)