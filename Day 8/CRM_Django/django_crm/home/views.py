from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    numbers={
        'fruits':['apple','banana']

    }
    return render(request,'index.html',numbers)

def about(request):
    return render(request,"about.html")

def booking(request):
    return HttpResponse("booking")

def form(request):
    return render(request,'form.html')