from django.urls import path

from . import views

urlpatterns = [
	path('adp', views.adp, name="pengunjung_adp"),
	path('pcdd', views.pcdd, name="pengunjung_pcdd"),
	path('pcde', views.pcde, name="pengunjung_pcde"),
	path('', views.index, name="pengunjung_index"),
]