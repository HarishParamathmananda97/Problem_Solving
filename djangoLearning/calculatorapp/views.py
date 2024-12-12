from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    print("Harry")
    return render(request, 'index.html')

def submitquery(request):
    q = request.GET['query']
    try:
        ans=eval(q)
        mydictionary = {
            'q' : q, 
            'ans': ans,
            'error' : False, 
            'result': True
        }
        # print(mydictionary)
        return render(request, 'index.html', context = mydictionary)
    
    except Exception as e:
        mydictionary={
            "error" : True,
            'errormsg': e ,
            'result': False,
        }
        # print(mydictionary)

        return render(request, 'index.html', context =mydictionary)

    # return HttpResponse(q)
    #     dict = {
    #     'result' : q
    # }
    # return JsonResponse(dict)