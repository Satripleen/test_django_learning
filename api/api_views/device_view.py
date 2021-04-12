from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Device
from api.serializers.device_serializer import DeviceSerializer


class DeviceListApiView(APIView):
    def get(self,request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("invalid_data")

class DeviceDetailsApiView(APIView):
    def get(self,request,id):
        try:
            device = Device.objects.get(id = id)
        except:
            return Response("Invalid data")
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def put(self,request,id):
        try:
            device = Device.objects.get(id = id)
        except:
            return Response("Invalid data")
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        try:
            device = Device.objects.get(id = id)
            device.delete()
            return Response("deleted")
        except:
            return Response("Invalid data")









