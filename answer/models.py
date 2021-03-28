from django.contrib.auth.models import User
from django.db import models
from question.models import Question
from interview.models import Interview
from question.models import QuestionOption


# создаем в базе полный опрос пройденный пользователем
class InterviewUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, verbose_name='Опрос')


# ответы на вопросы в опросе
class Answer(models.Model):
    interview_user = models.ForeignKey(InterviewUser, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.TextField(verbose_name='Текс ответа', null=True)


# выбраные варианты ответов
class AnswerOption(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_option')
    question_option = models.ForeignKey(
        QuestionOption, on_delete=models.CASCADE, verbose_name='Вариант ответа на вопрос', null=True
    )
