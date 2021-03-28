from rest_framework import serializers
from answer.models import InterviewUser, Answer, AnswerOption


class AnswerOptionSerializer(serializers.ModelSerializer):
    question_option = serializers.PKOnlyObject

    class Meta:
        model = AnswerOption
        fields = ('question_option',)


class AnswerSerializer(serializers.ModelSerializer):
    answer_option = AnswerOptionSerializer(many=True, required=False)

    class Meta:
        model = Answer
        fields = ('id', 'text', 'question', 'answer_option')
        read_only_fields = ('interview_user',)  # ответ будет создан в самой сериализации


class InterviewUserSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = InterviewUser
        fields = '__all__'

    def create(self, validated_data):
        answers = validated_data.pop('answers', [])  # получаем список ответов на вопросы
        interview_user = InterviewUser.objects.create(**validated_data)
        for answer in answers:
            question = answer['question']
            answer_create = Answer.objects.create(interview_user=interview_user, **answer)
            if question.type_answer == 'single' or question.type_answer == 'multi':
                options = answer['text'].split(',')
                for option in options:
                    AnswerOption.objects.create(question_option_id=option, answer=answer_create)
        return interview_user
