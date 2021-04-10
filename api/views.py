from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class Api(APIView):
    def get(self,request):
        return Response("get_test")

    def post(self,request):
        return Response(request.data)

    def put(self,request):
        return Response(request.data)

    def delete(self,request):
        return Response("delete_method")
