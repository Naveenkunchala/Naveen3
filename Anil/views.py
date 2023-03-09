from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def RoyalEnfield(request):
    return HttpResponse('My Favorate Bike')


def Himalayan(request):
    return HttpResponse('<h1>My Dream Bike</h1>')
