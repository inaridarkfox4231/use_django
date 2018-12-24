from django.test import TestCase

# Create your tests here.
# 未来の日付は最近ではないので、testを書いて確かめる。

import datetime
from django.utils import timezone

from .models import Question

print('test polls')
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)
        # Falseじゃないとエラーを返すみたいな。

# これを実行する。はいでました。
# 日付が過去である、という条件を加えて再実行する。
