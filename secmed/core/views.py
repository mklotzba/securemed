from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	template_name = 'core/home.html'
	context = {}
	return HttpResponse(render(request, template_name=template_name, context=context))
