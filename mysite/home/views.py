from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    # return HttpResponse("Hello world.")
    return render(request, 'home/hello.html')
