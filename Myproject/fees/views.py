from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def pay_fees(request):
    return HttpResponse("Semester fee is 40k")

def learn_python(request):
    return HttpResponse('<h1>Hello From Index page</h1>')