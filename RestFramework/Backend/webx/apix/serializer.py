from django.contrib.auth.models import User
from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Customer
        fields = ['name', 'age', 'gender', 'number']

    def get_number(self, obj):

        return obj.get_number


class UserSearializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
