from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')
def jadeja(request):
    return HttpResponse('<h2><i>Ravindra Jadeja is an all-rounder and he is a csk player in ipl</i></h2>')