from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    print("Reques: ",request)
    if(request == 'index'):
        return HttpResponse("Hello, world. You're at the polls index.")
    else:
        return HttpResponse("No")

    
        