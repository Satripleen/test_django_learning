from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Device
from api.serializers.device_serializer import DeviceSerializer


class DeviceApiView(APIView):
    def get(self,request):
        devices = Device.objects.all()
        devices = [ {"name": device.name} for device in devices ]
        return Response(devices)

    def post(self,request):
        data = request.data
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            device = Device()
            device.name= data.get("name")
            device.device_tag = data.get("device_tag")
            device.save()
            return Response({"name": device.name})
        return Response("invalid_data")





