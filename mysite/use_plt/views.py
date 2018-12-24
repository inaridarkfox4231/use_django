from django.shortcuts import render

from django.http import HttpResponse
import io
import matplotlib.pyplot as plt
import numpy as np

def index(request):
    return render(request, 'use_plt/index.html')

def show_plot(request, pk):
    context = {'pk': pk}
    return render(request, 'use_plt/plot.html', context)

def set_plt(pk):
    if pk is 1:
        fig = plt.figure()
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([10, 20, 30, 40, 50])
        plt.plot(x, y)
        plt.title("simple")

    if pk is 2:
        fig = plt.figure()
        x = np.linspace(-2, 2, 100)
        y = x ** 2
        plt.plot(x, y)
        plt.title(r'$y={x}^2$')

    if pk is 3:
        fig = plt.figure()
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([50, 40, 30, 20, 10])
        plt.plot(x, y)
        plt.title("simple")

def plt_to_svg():
    buf = io.BytesIO()
    plt.savefig(buf, format = 'svg', bbox_inches = 'tight')
    s = buf.getvalue()
    buf.close()
    return s

def get_svg(request, pk):
    set_plt(pk)            # create the plot
    svg = plt_to_svg()   # convert plot to SVG
    plt.cla()            # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type = 'image/svg+xml')
    return response
