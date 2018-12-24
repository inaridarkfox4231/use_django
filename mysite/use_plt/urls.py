from django.urls import path

from . import views

app_name = 'use_plt'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('show_plot/<int:pk>', views.show_plot, name = 'show_plot'),
    path('plot/<int:pk>/', views.get_svg, name = 'plot'),
]
