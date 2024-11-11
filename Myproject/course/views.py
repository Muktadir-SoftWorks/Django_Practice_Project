from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_python(request):
    return render(request, 'course_python.html')

def calculate(request):
    return HttpResponse('I am calculator')