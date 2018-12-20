from django.http import HttpResponse
# ちょっとした実験

def hello(request):
    return HttpResponse("Hello world. Good Job!")
