from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from myapp.models import *

def index(request):
	context = {}
	return render(request, 'pengunjung/index.html', context)

def adp(request):
	if request.method == "POST":
		data = request.POST
		file = request.FILES.getlist('filenya')

		t = Tugas(nama=data['nama'], nim=data['nim'], kelas="c", subjek=data['subjek'])
		t.save()

		for value in file:
			file_t = FileTugas(tugas=t, filenya=value)
			file_t.save()

		return redirect('pengunjung_adp')

	context = {}
	return render(request, 'pengunjung/adp.html', context)

def adp_subjek(request, subjek):
	context = {}
	return HttpResponse('oke')

def pcdd(request):
	if request.method == "POST":
		data = request.POST
		file = request.FILES.getlist('filenya')

		t = Tugas(nama=data['nama'], nim=data['nim'], kelas="d", subjek=data['subjek'])
		t.save()

		for value in file:
			file_t = FileTugas(tugas=t, filenya=value)
			file_t.save()

		return redirect('pengunjung_pcdd')
	context = {}
	return render(request, 'pengunjung/pcdd.html', context)

def pcde(request):
	if request.method == "POST":
		data = request.POST
		file = request.FILES.getlist('filenya')

		t = Tugas(nama=data['nama'], nim=data['nim'], kelas="e", subjek=data['subjek'])
		t.save()

		for value in file:
			file_t = FileTugas(tugas=t, filenya=value)
			file_t.save()

		return redirect('pengunjung_pcde')
	context = {}
	return render(request, 'pengunjung/pcde.html', context)