from django.http import HttpResponse
from django.shortcuts import render


def enroll(request):
    return HttpResponse('Hello I am successfully enrolled')

# Create your views here.
def T_enroll(request):
    context = {'ins_name':'Sadat'}
    return render(request, 'student_html/course.html', context)
