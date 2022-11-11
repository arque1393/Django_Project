from dataclasses import field
from os import read
from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Customer
        fields = ['name', 'age', 'gender', 'number']

    def get_number(self, obj):

        return obj.get_number
