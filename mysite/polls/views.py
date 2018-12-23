from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
# from django.template import loader

from .models import Question

def index(request):
    text = "直近の質問5つを新しい順に表示"
    list = Question.objects.order_by('-pub_date')[:5]
    context = {
      'title_text': text, # title_textは変数展開{{}}でindex.htmlに埋め込まれている
      'latest_question_list': list, # latest_question_listはfor文の形で埋め込み。
    }
    return render(request, 'polls/index.html', context)

# 新しいビュー関数を追加
def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/detail.html", {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
