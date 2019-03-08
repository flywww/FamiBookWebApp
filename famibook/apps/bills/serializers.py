from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'  # can set different column ('id', 'name')
