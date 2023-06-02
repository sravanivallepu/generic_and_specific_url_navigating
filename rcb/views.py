from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def siraj(request):
    return HttpResponse('<h2><marquee><i> siraj is a bowler in ipl </i></marquee></h2><br>')