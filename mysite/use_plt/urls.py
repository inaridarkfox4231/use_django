from django.urls import path

from . import views

app_name = 'use_plt'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('plot/<int:pk>/', views.get_svg, name = 'plot'),
]
