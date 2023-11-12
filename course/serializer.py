from rest_framework import serializers
from .models import Earning
from django.contrib.auth import get_user_model

User = get_user_model()

class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = '__all__'

