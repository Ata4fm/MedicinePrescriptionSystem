from rest_framework import serializers
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category_name'] = instance.category.name  # مقدار دلخواه را اضافه کنید
        return representation