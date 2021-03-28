from rest_framework import serializers
from question.models import Question, QuestionOption
# from interview.serializers import InterviewSerializer


class QuestionOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionOption
        fields = ('text',)


class QuestionSerializer(serializers.ModelSerializer):
    option = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = '__all__'
