import jalali_date
from rest_framework import serializers
from .models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['doctor'] = instance.doctor.get_full_name()
        representation['created_date'] = str(jalali_date.date2jalali(instance.created_date))
        return representation
