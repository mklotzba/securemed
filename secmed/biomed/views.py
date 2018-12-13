from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def biomed(request):
	template_name = 'biomed/biomed.html'
	context = {}
	return HttpResponse(render(request, template_name=template_name, context=context))
