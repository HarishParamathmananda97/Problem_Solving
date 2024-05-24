from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Welcome Back django Master Harish Paramathmananda.")

def myfunctionabout(request):
    return HttpResponse("<h1>Welcome to about page Master Harry</h1>")

def myfunctionadd(request, a, b):
    return HttpResponse(f"Your requested addition answer is for {a} + {b} = {a + b}")

def intro(request, name, age):
    mydict = {
        "name":name, 
        "age": age
    }
    return JsonResponse(mydict)
    # return HttpResponse(f" Welcome back Mr.{name} and you are {age} years old ")