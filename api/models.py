from django.db import models
from django.contrib.auth.models import User

GENERAL = 0
BOOK_MARKED = 1

BOOK_MARK_STATUS = (
    (GENERAL, 'General'),
    (BOOK_MARKED, 'Book Marked')
)


class Question(models.Model):
    posted_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='questions')
    questions = models.CharField(
        max_length=255, verbose_name='Questions')
    book_mark = models.IntegerField(
        verbose_name='Book Mark', default=GENERAL, choices=BOOK_MARK_STATUS)


class Answer(models.Model):
    answered_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='replies')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    answers = models.CharField(
        max_length=255, verbose_name='Answers')
    book_mark = models.IntegerField(
        verbose_name='Book Mark', default=GENERAL, choices=BOOK_MARK_STATUS)
