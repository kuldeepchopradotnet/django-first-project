from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    '''return HttpResponse("hello this is my first project http response")'''
    return render(request, 'home.html')