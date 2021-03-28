from django.db import models
from interview.models import Interview
from question.choices import TYPE_ANSWER_CHOICES


class Question(models.Model):
    interview = models.ForeignKey(Interview, related_name='question', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст вопроса')
    type_answer = models.CharField(choices=TYPE_ANSWER_CHOICES, max_length=16, default='text')


class QuestionOption(models.Model):
    class Meta:
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='option', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='Текст варианта ответа')

    def __str__(self):
        return self.text
