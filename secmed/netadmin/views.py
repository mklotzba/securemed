from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def netadmin(request):
	template_name = 'netadmin/netadmin.html'
	context = {}
	return HttpResponse(render(request, template_name=template_name, context=context))