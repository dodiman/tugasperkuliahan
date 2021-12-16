from django import forms
from myapp.models import *

class PencarianForm(forms.Form):
	kata_kunci = forms.CharField(max_length=100)

class FileTugasForm(forms.ModelForm):
	class Meta:
		model = FileTugas
		fields = '__all__'

class SubjekForm(forms.ModelForm):
	class Meta:
		model = Subjek
		fields = '__all__'