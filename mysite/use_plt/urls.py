from django.urls import path

from . import views

app_name = 'use_plt'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('show_plot/<int:pk>/', views.show_plot, name = 'show_plot'),
    path('plot/<int:pk>/', views.get_svg, name = 'plot'),
    path('make_plot/', views.make_plot, name = 'make_plot' ),
    path('plot_2/<ind_3>/<ind_2>/<ind_1>/<ind_0>/', views.get_svg_custom, name = 'plot_2'),
]
