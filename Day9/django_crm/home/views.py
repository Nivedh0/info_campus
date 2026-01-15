from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,"about.html")

def booking(request):
    return HttpResponse("booking")

def form(request):
    return render(request,'form.html')

def customer_list(request): 
    customer_list = [
        {"name": "Arun", "email": "arun@gmail.com", "status": "Lead"},
        {"name": "Meera", "email": "meera@gmail.com", "status": "Customer"},
    ]

    return render(request, "customer.html", {"customers": customer_list})
