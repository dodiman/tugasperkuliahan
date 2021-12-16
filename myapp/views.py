from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {}
	return render(request, 'myapp/index.html', context)

def adp(request):
	context = {}
	return render(request, 'myapp/adp.html', context)

def pcdd(request):
	context = {}
	return render(request, 'myapp/pcdd.html', context)

def pcde(request):
	context = {}
	return render(request, 'myapp/pcde.html', context)