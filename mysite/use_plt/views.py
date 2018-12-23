from django.shortcuts import render

from django.http import HttpResponse
from use_plt.maketext import make_greet

def index(request):
    return render(request, 'use_plt/index.html')

def greet(request, your_name):
    return HttpResponse(make_greet(your_name))
