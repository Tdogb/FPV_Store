from django.http import HttpResponse
from django.shortcuts import render
from django.db import models

def homePage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')