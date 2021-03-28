from rest_framework import serializers
from interview.models import Interview
from question.serializers import QuestionSerializer


class InterviewSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = Interview
        fields = '__all__'
