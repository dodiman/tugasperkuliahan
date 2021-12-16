from django.db import models

class Subjek(models.Model):
	nama_subjek = models.CharField(max_length=100, unique=True)
	batas_waktu = models.DateTimeField()
	matakuliah = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_updated = models.DateTimeField(auto_now=True, null=True)

class Tugas(models.Model):
	nama = models.CharField(max_length=100, null=True)
	nim = models.CharField(max_length=100, null=True, unique=True)
	kelas = models.CharField(max_length=100, null=True)
	absen = models.CharField(max_length=100, null=True, unique=True)
	subjeks = models.ManyToManyField(Subjek)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_updated = models.DateTimeField(auto_now=True, null=True)

class FileTugas(models.Model):
	tugas = models.ForeignKey(Tugas, on_delete=models.CASCADE, null=True)
	filenya = models.FileField(upload_to="file/%Y/%m/%d")
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_updated = models.DateTimeField(auto_now=True, null=True)


