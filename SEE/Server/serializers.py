from django.contrib.auth.models import User,Group
import models
from rest_framework import serializers

class DoctorSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ('url', 'username')

class PatientSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Patient
        fields = ('url', 'username') 
