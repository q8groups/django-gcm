from rest_framework import serializers

from .models import Device


class DeviceSerialzer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(default=True)
    class Meta:
        model = Device
        fields = ('dev_id', 'reg_id','is_active',)


