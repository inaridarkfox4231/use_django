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

def make_plot(request):
    # 数に変換できない時は多分ここでバリデーションする必要が・・
    try:
        context = {'ind_3': request.POST['ind_3'],
                   'ind_2': request.POST['ind_2'],
                   'ind_1': request.POST['ind_1'],
                   'ind_0': request.POST['ind_0']}
    except:
        context = {'ind_3': 0, 'ind_2': 0, 'ind_1': 0, 'ind_0': 1 }
    return render(request, 'use_plt/plot_2.html', context)

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

def str_sign(x):
    if x >= 0:
        return "+" + str(x)
    else:
        return str(x)

def make_plt(a = 0, b = 0, c = 0, d = 1):
    fig = plt.figure()
    x = np.linspace(-5, 5, 100)
    y = a * x * x * x + b * x * x + c * x + d
    plt.plot(x, y)
    plt.title("y=" + str(a) + r'$x^3$' + str_sign(b) + r'$x^2$' + str_sign(c) + r'$x$' + str_sign(d))

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

def get_svg_custom(request, ind_3, ind_2, ind_1, ind_0):
    # ここもバリデーションするか、doubleでやるかどっちか。
    # 文字列とかね、不正な入力に対してメッセージ表示して同じページに戻るようにする。
    # あっちのLTやLT_2もそうする方がいいかもね。そうするほどのアプリじゃないけども。
    make_plt(int(ind_3), int(ind_2), int(ind_1), int(ind_0))
    svg = plt_to_svg()
    plt.cla()
    response = HttpResponse(svg, content_type = 'image/svg+xml')
    return response
