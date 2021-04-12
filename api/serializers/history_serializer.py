from rest_framework import serializers

from api.models import Customer, History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["id","customer","device","units","price"]