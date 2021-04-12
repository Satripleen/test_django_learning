from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Customer
from api.serializers.customer_serializer import CustomerSerializer


class CustomerListApiView(APIView):
    def get(self,request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("invalid_data")

class CustomerDetailsApiView(APIView):
    def get(self,request,id):
        try:
            customer = Customer.objects.get(id = id)
        except:
            return Response("Invalid data")
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self,request,id):
        try:
            customer = Customer.objects.get(id = id)
        except:
            return Response("Invalid data")
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        try:
            customer = Customer.objects.get(id = id)
            customer.delete()
            return Response("deleted")
        except:
            return Response("Invalid data")









