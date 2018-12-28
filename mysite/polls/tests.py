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
# テスト追加。
# テスト1: 1日と1秒前の場合に「古い」と認識されるか
# テスト2: 23時間59分59秒前の場合に「新しい」と認識されるか

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
