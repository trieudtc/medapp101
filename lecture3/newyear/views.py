from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/isnewyear.html", {
        "newyear": now.day == 1 and now.month == 1 
    })
