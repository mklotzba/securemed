from django.shortcuts import render
from django.http import HttpResponse
from secmed.integration import models
from .forms import IseForm

# Create your views here.

def integration(request):
	template_name = 'integration/integration.html'
	form = IseForm()
	context = {'form':form}
	return HttpResponse(render(request, template_name=template_name, context=context))
'''
def integration(request):
	return HttpResponse("hi there")
'''