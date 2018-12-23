# use_django
django使ってみる  
http://127.0.0.1:8000 にアクセスするとローカルで確認できる。  
bat: dj.batからcd mysiteでrun.batで実行、Ctrl-Cで終了。  

staticを利用した画像の表示。  
ステップ0: use_plt直下にstaticフォルダを作成し、そこに表示したい画像（たとえば***.png）を入れる。  
ステップ1：settingsにdjango.contrib.staticfilesが入ってることを確認（もう入ってる）。  
ステップ2：settingsの中でSTATIC/URL = "/static/"と記述（もうなってる）  
ステップ3：html側で、{% load static %}したのち、たとえばimgタグに放り込むとして、  
          <img src = "{% static "***.jpg" %}" alt = "My_image">  
          とかすると表示されるよ（altは画像が表示されない場合の説明用テキスト）。  

matplotlibで打ち出した画像を表示する方法。  
以下のサイトを参考にさせていただきました。感謝します。  
http://intellectual-curiosity.tokyo/2018/10/30/djangoでmatplotlibによるグラフ表示する方法/  
アプリ名はuse_pltとする。  
まず、urls.pyでviewsのところにsvgという形式でグラフを返す関数を用意する。こんな感じ：  
path('plot/', views.get_svg, name = 'plot'),  
次に、views.pyでget_svgを定義する。  
from django.http import HttpResponse  
import io  
import matplotlib.pyplot as plt  
import numpy as np  

手順1: pltにグラフを用意する  
def set_plt():  
    x = np.array([1, 2, 3, 4, 5])  
    y = np.array([10, 20, 30, 40, 50])  
    plt.plot(x, y)  

手順2: pltからsvgにconvertする（io使う）  
def plt_to_svg():  
    buf = io.BytesIO()  
    plt.savefig(buf, format = 'svg', bbox_inches = 'tight')  
    s = buf.getvalue()  
    buf.close()  
    return s  

io.BytesIO()はbytes-likeオブジェクトをbytesオブジェクトにするらしい・・  

手順3: svgをresponseとして返す。  
def get_svg():  
    set_plt()  
    svg = plt_to_svg()  
    plt.cla()  # クリーンアップ  
    response = HttpResponse(svg, content-type = "image/svg+xml") # svgだとだめで+xmlが必要だった  
    return response  

調べたらimage/svgというMIMEタイプは存在しなくて、image/svg+xmlで型になってた。なるほどねー。  
タイトル付けようと思ったんだけど、  
plt.plot(x, y)  
のあとにplt.title("simple")ってやらないといけないのね・・先にやるとエラーになる。  
