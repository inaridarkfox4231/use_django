from django.http import HttpResponse
# ちょっとした実験
from django.template import loader

def hello(request):
    return HttpResponse("Hello world.")
