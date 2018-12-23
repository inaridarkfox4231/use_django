from django.urls import path

from . import views

app_name = 'use_plt'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug:your_name>/greet', views.greet, name = 'greet')
]
