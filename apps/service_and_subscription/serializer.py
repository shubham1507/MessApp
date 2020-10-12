from rest_framework import serializers

from .models import ServiceAndSubscription


class ServiceSubscribeSerializer(serializers.ModelSerializer):
    class Meta:

        model = ServiceAndSubscription
        fields = '__all__'
