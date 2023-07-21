from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def core(request):
    return HttpResponse("Hello World")

# Create your views here.
