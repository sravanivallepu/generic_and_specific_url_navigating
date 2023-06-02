from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sehwag(request):
    return render(request,'sehwag.html')

def hardik(request):
    return HttpResponse('<h2><i><marquee>Hardik is a best all-rounder in india team.<br>He is also a captain of Gujarat Titans in IPL.</marquee></i></h2>')
