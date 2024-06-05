from .forms import *
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

def myfirstpage(request):
    return render(request, 'index.html') 

def mysecondpage(request):
    return render(request, 'second.html') 
def mythirdpage(request, a, b):
    var = "Hello Master, Harry!"
    greeting = "hey, How are you Jerry..."
    fruits = ["apple", "mango", "banana"]
    # num1, num2 = 2, 5
    num1, num2 = a, b
    ans = num1 > num2
    print(ans)
    mydict = {
        "var" : var, 
        "msg" : greeting,
        "myfruits" : fruits,
        "num1" :  num1, 
        "num2" : num2,
        "ans" : ans
    }
    return render(request, 'third.html', context = mydict) 

def myimagepage(request):
    return render(request, 'imagepage.html')

def myimagepage2(request):
    return render(request, 'imagepage2.html')

def myform(request):
    return render(request, 'myform.html')

# def mysubmittedform(request):
#     print(request)
#     mydict = {
#         'mytext' : request.GET['mytext'],
#         'mytextarea': request.GET['mytextarea'],

#         'method': request.method,
#     }
#     print(mydict)
#     return JsonResponse(mydict)

def mysubmittedform(request):
    print(request)
    mydict = {
        'mytext' : request.POST['mytext'],
        'mytextarea': request.POST['mytextarea'],
        'method': request.method,
    }
    print(mydict)
    return JsonResponse(mydict)


def myform2(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            print(title, subject)
            var = str(f"Form submitted {request.method}")
            
        return HttpResponse(var)
    elif request.method == 'GET':
        form = FeedbackForm()  # FeedbackForm(None)
        mydictionary = {
            'form' : form
        }
        return render(request, 'myform2.html', context = mydictionary)