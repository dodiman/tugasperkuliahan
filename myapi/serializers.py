from rest_framework import serializers
from myapp.models import *

# class TugasSerializer(serializers.Serializer):
# 	nama = serializers.CharField(max_length=100)
# 	nim = serializers.CharField(max_length=100)
# 	kelas = serializers.CharField(max_length=100)
# 	subjek = serializers.CharField(max_length=100)

class TugasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tugas
		fields = '__all__'

class FileTugasSerializer(serializers.ModelSerializer):
	class Meta:
		model = FileTugas
		fields = '__all__'

class SubjekSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subjek
		fields = '__all__'