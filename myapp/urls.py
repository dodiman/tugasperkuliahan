from django.urls import path

from . import views

urlpatterns = [
	path('adp', views.adp, name="myapp_adp"),
	path('pcdd', views.pcdd, name="myapp_pcdd"),
	path('pcde', views.pcde, name="myapp_pcde"),
	path('', views.index, name="myapp_index"),
]