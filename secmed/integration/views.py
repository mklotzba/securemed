from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def integration(request):
	template_name = 'integration/integration.html'
	context = {}
	return HttpResponse(render(request, template_name=template_name, context=context))