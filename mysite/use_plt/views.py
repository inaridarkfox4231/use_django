from django.http import HttpResponse
from use_plt.maketext import make_greet

def index(request):
    return HttpResponse("matplotlibでなんか作りたいです")

def greet(request, your_name):
    return HttpResponse(make_greet(your_name))
