from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import History, Customer, Device
from api.serializers.history_serializer import HistorySerializer


class HistoryListApiView(APIView):
    def get(self,request):
        historys = History.objects.all()
        serializer = HistorySerializer(historys, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = HistorySerializer(data=data)

        try:
            Customer.objects.get(phone_number = data["customer"])
            device = Device.objects.get(device_tag = data["device"])
        except:
            return Response("Invaid Data")
        price = int(data["units"]) * device.price

        if serializer.is_valid():
            history = serializer.save()
            history.price = price
            history.save()
            serializer = HistorySerializer(history)
            return Response(serializer.data)
        return Response("invalid_data")

# class HistoryDetailsApiView(APIView):
#     def get(self,request,id):
#         try:
#             history = History.objects.get(id = id)
#         except:
#             return Response("Invalid data")
#         serializer = HistorySerializer(history)
#         return Response(serializer.data)
#
#     def put(self,request,id):
#         try:
#             history = History.objects.get(id = id)
#         except:
#             return Response("Invalid data")
#         serializer = HistorySerializer(history, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#     def delete(self,request,id):
#         try:
#             history = History.objects.get(id = id)
#             history.delete()
#             return Response("deleted")
#         except:
#             return Response("Invalid data")









