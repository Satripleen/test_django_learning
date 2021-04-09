from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

# def home(request):
#    return HttpResponse("Hello Home")

class Home(View):
    def get(self,request):
        return render(request,"index.html")

    def post(self,request):
        print(request.POST)
        return render(request,"index.html", {"name": request.POST.get("name")})
