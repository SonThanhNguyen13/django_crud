from .models import DataTable
from rest_framework import serializers

class DataForm(serializers.ModelSerializer):
    class Meta():
        model = DataTable
        fields = '__all__'
