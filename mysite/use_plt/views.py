from django.shortcuts import render

from django.http import HttpResponse
import io
import matplotlib.pyplot as plt
import numpy as np

def index(request):
    return render(request, 'use_plt/index.html')

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
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = Axes3D(fig)
        X = np.arange(-4, 4, 0.25)
        Y = np.arange(-4, 4, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(7 * (X ** 2) + 2 * (Y ** 2))
        Z = np.sin(R)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
        ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
        ax.set_zlim(-2, 2)
        plt.title(r'${Z}^2 = 7{X}^2 + 2{Y}^2$')

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
