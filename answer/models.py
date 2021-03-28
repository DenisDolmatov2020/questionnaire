from django.contrib.auth.models import User
from django.db import models
from question.models import Question
from interview.models import Interview
from question.models import QuestionOption


# создаем в базе полное интервью пройденное пользователем
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, verbose_name='Опрос')


# выбранные варианты ответов на вопросы в опросе
class AnswerOption(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_items')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.TextField(verbose_name='Текс ответа', null=True)
    option = models.ForeignKey(QuestionOption, on_delete=models.CASCADE, verbose_name='Вариант ответа', null=True)
