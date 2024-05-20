from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rawtang, Rawramp, Rawkes, ChartRaw

class RawtangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rawtang
        fields = "__all__"

class RawrampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rawramp
        fields = "__all__"

class RawkesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rawkes
        fields = "__all__"

class ChartRawSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartRaw
        fields = "__all__"