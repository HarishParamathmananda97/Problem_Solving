from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def root(request):
    print("Harry")
    return HttpResponse('Welcome back Master, Server is started.')