from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt 

from myapi.serializers import *
from myapi.forms import *

from datetime import datetime, timedelta
from django.utils import timezone
import pytz

# autentifikasi
from django.contrib.auth.decorators import login_required

@csrf_exempt
def index_data(request):
	if request.method == 'GET':
		db = Tugas.objects.all()
		serializer = TugasSerializer(db, many=True)
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		# data = JSONParser().parse(request)
		data_post = request.POST
		"""
		1. mengecek nama sudah ada atau belum
		2. jika ada ===> update
		3. jika tidak ada ===> create
		"""
		try: 
			db = Tugas.objects.get(nim=data_post['nim'])
			serializer = TugasSerializer(db, data=data_post)
			if serializer.is_valid():
				serializer.save()
			return JsonResponse(serializer.data)
		except Tugas.DoesNotExist:
			serializer = TugasSerializer(data=data_post)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def update_tugas(request, id):
	try:
		db = Tugas.objects.get(pk=id)
	except Tugas.DoesNotExist:
		return HttpResponse(status=404)
	
	if request.method == 'GET':
		serializer = TugasSerializer(db)
		return JsonResponse(serializer.data)

	if request.method == 'POST':
		# data = JSONParser().parse(request.data)
		data = request.POST
		serializer = TugasSerializer(db, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def delete_tugas(request):
	if request.method == 'GET':
		return HttpResponse(status=400)

	if request.method == 'POST':
		mydata = request.POST.getlist('id')
		db = Tugas.objects.filter(pk__in=mydata)
		if len(db) > 0:
			db = Tugas.objects.filter(pk__in=mydata)
			db.delete()
			return HttpResponse(status=204)
		return HttpResponse(status=400)


@csrf_exempt
def delete_tugas_all(request):
	if request.method == 'GET':
		return HttpResponse(status=400)

	if request.method == 'POST':
		db = Tugas.objects.all()
		db.delete()
		return HttpResponse(status=204)


def pesan_error(request, pesan):
	return JsonResponse({"pesan": pesan})

@csrf_exempt
def pencarian(request):
	if request.method == 'GET':
		return HttpResponse(status=400)

	if request.method == 'POST':
		form = PencarianForm(request.POST or None)
		if form.is_valid():
			data = request.POST['kata_kunci']
			# db = Tugas.objects.filter(nim__contains=data)
			db = Tugas.objects.filter(nim__iexact=data)
			if len(db) > 0:
				serializer = TugasSerializer(db, many=True)
				return JsonResponse(serializer.data, safe=False)
			else:
				return redirect("myapi_pesan_error", pesan="data tidak ditemukan")

		return redirect("myapi_pesan_error", pesan="data tidak ditemukan")


@csrf_exempt
def delete_tugas_file(request, id):
	if request.method == 'GET':
		return HttpResponse(status=400)

	if request.method == 'POST':
		mydata = request.POST.getlist('id')
		db = FileTugas.objects.filter(pk__in=mydata)
		db.delete()
		return HttpResponse(status=204)

@csrf_exempt
def create_file(request):
	db = FileTugas.objects.all()
	serializer = FileTugasSerializer(db, many=True)

	if request.method == 'GET':
		# db = FileTugas.objects.all()
		# serializer = FileTugasSerializer(db, many=True)
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		data_post = request.POST
		file_tugas = request.FILES.getlist('filenya')
		waktu_sekarang = timezone.now()

		try:
			subjek = Subjek.objects.get(pk=data_post['subjeks'])
		except Subjek.DoesNotExist:
			return HttpResponse(status=404)
		
		batas_waktu = subjek.batas_waktu
		batas_waktu = batas_waktu.replace(tzinfo=pytz.UTC)

		if (waktu_sekarang > batas_waktu):  # jika batas waktu lewat
			return HttpResponse(status=404)
			# return JsonResponse(form.errors, safe=False, status=400)

		"""
		1. cek nim sudah ada atau belum
		2. jika sudah ada tidak disimpan dan jika ada disimpan
		"""
		cek_data = Tugas.objects.filter(nim__iexact=data_post['nim'])
		if not cek_data:  # jika kosong
			kt = Tugas(
					nama = data_post['nama'],
					nim = data_post['nim'],
					kelas = data_post['kelas'],
					absen = data_post['absen'],
				)
			kt.save()
		else:
			kt = cek_data.first()

		# many to many Tugas to Subjek
		kt.subjeks.add(subjek)

		# menyimpan file tugas (multiply)
		for value in file_tugas:
			gbr_kt = FileTugas(
					tugas=kt,
					filenya=value
				)
			gbr_kt.save()
		return JsonResponse(serializer.data, safe=False, status=201)


# subjek crud

@csrf_exempt
def index_data_subjek(request):
	if request.method == 'GET':
		db = Subjek.objects.all()
		serializer = SubjekSerializer(db, many=True)
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		# data = JSONParser().parse(request)
		data = request.POST
		serializer = SubjekSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def update_subjek(request, id):
	try:
		db = Subjek.objects.get(pk=id)
	except Subjek.DoesNotExist:
		return HttpResponse(status=404)
	
	if request.method == 'GET':
		serializer = SubjekSerializer(db)
		return JsonResponse(serializer.data)

	if request.method == 'POST':
		data = request.POST
		serializer = SubjekSerializer(db, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def delete_subjek(request):
	if request.method == 'GET':
		return HttpResponse(status=400)

	if request.method == 'POST':
		mydata = request.POST.getlist('id')
		db = Subjek.objects.filter(pk__in=mydata)
		if len(db) > 0:
			db = Subjek.objects.filter(pk__in=mydata)
			db.delete()
			return HttpResponse(status=204)
		return HttpResponse(status=400)


@csrf_exempt
def delete_subjek_all(request):
	if request.method == 'GET':
		return HttpResponse(status=400)

	if request.method == 'POST':
		db = Subjek.objects.all()
		db.delete()
		return HttpResponse(status=204)

@csrf_exempt
def pencarian_subjek(request):
	if request.method == 'GET':
		return HttpResponse(status=400)

	if request.method == 'POST':
		form = PencarianForm(request.POST or None)
		if form.is_valid():
			data = request.POST['kata_kunci']
			# db = Subjek.objects.filter(nim__contains=data)
			db = Subjek.objects.filter(nama_subjek__iexact=data)
			if len(db) > 0:
				serializer = SubjekSerializer(db, many=True)
				return JsonResponse(serializer.data, safe=False)
			else:
				return redirect("myapi_pesan_error", pesan="data tidak ditemukan")

		return redirect("myapi_pesan_error", pesan="data tidak ditemukan")

# end subjek


def pesan_error(request, pesan):
	return JsonResponse({"pesan": pesan})

@csrf_exempt
def contoh(request):
	if request.method == 'GET':
		form = SubjekForm()
		db = Subjek.objects.last()
		waktu_sekarang = timezone.now()
		# tz = pytz.timezone('Asia/Jakarta')
		# waktu_sekarang = waktu_sekarang.replace(tzinfo=tz)
		batas_waktu = db.batas_waktu
		batas_waktu = batas_waktu.replace(tzinfo=pytz.UTC)

		context = {
			'form': form,
		}
		# print(f"\n\n")
		# print(f"waktu sekarang django:\n {waktu_sekarang_django}")
		# print(f"waktu sekarang django2:\n {waktu_sekarang_django2}")
		# print(f"waktu sekarang2:\n {waktu_sekarang2}")
		# print(f"waktu sekarang:\n {waktu_sekarang+timedelta(hours=8)}")
		# print(f"batas waktu:\n {batas_waktu+timedelta(hours=8)}")
		# print(f"db:\ndate created: {db.date_created}\ndate updated: {db.date_updated}")
		# print(f"\n\n")
		if (waktu_sekarang <= batas_waktu):
			return HttpResponse('masih bisa kirim tugas')
			# return HttpResponse(form)
			# return render(request, 'contoh.html', context)
		else:
			# return HttpResponse(form)
			return HttpResponse('batas waktu telah berlalu')
			# return render(request, 'contoh.html', context)

	if request.method == 'POST':
		# form = SubjekForm(request.POST or None)
		# print(f"request:\n{request.POST}")
		# if form.is_valid():
		# 	print(f"form is valid: True")
		# 	print(f"form:\n{form}")
		# 	# form.save()
		# return redirect('contoh')
		
		subjek = Subjek.objects.get(pk=9)
		return HttpResponse('coba contoh')
