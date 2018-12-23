from django.shortcuts import render

from django.http import HttpResponse
import io
import matplotlib.pyplot as plt
import numpy as np

def index(request):
    return render(request, 'use_plt/index.html')

def set_plt(pk):
    if pk is 1:
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([10, 20, 30, 40, 50])
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
