from django.shortcuts import render
from django.http import HttpResponse

# def print(request):
#     return HttpResponse("Hello Camapp")
def print(request):
    movie={
        'title':'premalu',
        'summary':'nil',
        'year':'2024',
        'sucess':True
    }
    return render(request,'hello.html',movie)