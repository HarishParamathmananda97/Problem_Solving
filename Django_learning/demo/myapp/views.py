from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Welcome to FactEntry!  Lets Do Great things together.")
    return render(request, 'home.html')