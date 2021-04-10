from rest_framework import serializers


class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, min_length=3)
    device_tag = serializers.CharField(max_length=10, min_length=3)
    created_at = serializers.DateTimeField(read_only=True)