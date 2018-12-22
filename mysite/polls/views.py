from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.template import loader

from .models import Question

def index(request):
    text = "直近の質問5つを新しい順に表示"
    list = Question.objects.order_by('-pub_date')[:5]
    subject = "数学"
    score = "100"
    context = {
      'title_text': text, # title_textは変数展開{{}}でindex.htmlに埋め込まれている
      'latest_question_list': list, # latest_question_listはfor文の形で埋め込み。
      'subject': subject,
      'score': score,
    }
    return render(request, 'polls/index.html', context)

# 新しいビュー関数を追加
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, "polls/detail.html", {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
