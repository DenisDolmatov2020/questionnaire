from rest_framework import serializers
from question.models import Question, QuestionOption


class QuestionOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionOption
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    option = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ('text', 'type_answer', 'option')
