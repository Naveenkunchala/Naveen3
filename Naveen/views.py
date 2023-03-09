from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def Charan(request):
    return HttpResponse('<h1>My Hero</h1>')


def chiru(request):
    return HttpResponse('<h1>My Hero father</h1>')
