from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['code','first_name','last_name','phonenumber','age','address','file','gender','information']