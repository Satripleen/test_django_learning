from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Device


class DeviceApiView(APIView):
    def get(self,request):
        devices = Device.objects.all()
        devices = [ {"name": device.name} for device in devices ]
        return Response(devices)





