import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
        # ↑ now >= を追加して、「過去である」ということを示す。
        # 仕様：過去の質問で今この瞬間から1日以内に投稿された場合にtrueを返す感じ。

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text

# 各々のクラス変数はデータベースのフィールドを表している。
# ForeignKeyで関連付けを表している。
