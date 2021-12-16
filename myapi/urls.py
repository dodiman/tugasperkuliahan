from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()

from . import views

# model: Tugas {nama, nim, kelas, subjek}
# model: FileTugas {tugas, filenya}

urlpatterns = [
	path('delete_tugas_all', views.delete_tugas_all, name="myapi_delete_all"), # d semua
	path('delete_tugas', views.delete_tugas, name="myapi_delete"), # d
	path('update_tugas/<str:id>', views.update_tugas, name="myapi_update"), # u
	path('tugas', views.index_data, name="myapi_index"), # c,r
	path('pencarian', views.pencarian, name="pencarian"), # pencarian
	path('contoh', views.contoh, name="contoh"), # contoh

	path('subjek', views.index_data_subjek, name="myapi_index_subjek"), # c,r
	path('update_subjek/<str:id>', views.update_subjek, name="myapi_update_subjek"), # u
	path('delete_subjek', views.delete_subjek, name="myapi_delete_subjek"), # d
	path('delete_subjek_all', views.delete_subjek_all, name="myapi_delete_all_subjek)"), # d semua
	path('pencarian_subjek', views.pencarian_subjek, name="pencarian_subjek"), # pencarian

	path('delete_tugas_file/<str:id>', views.delete_tugas_file, name="myapi_delete_file"), # d
	path('create_file', views.create_file, name="myapi_create_file"), # create_file

	path('pesan_error/<str:pesan>', views.pesan_error, name="myapi_pesan_error"), # pesan error
	
]

urlpatterns += router.urls