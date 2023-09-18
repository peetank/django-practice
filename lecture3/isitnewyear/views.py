from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

def index(request):
    today = date.today()
    
    return render(request, "isitnewyear/index.html", {
        "newyear" : today.day == 1 and today.month == 1
        })
