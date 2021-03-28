from rest_framework import serializers
from answer.models import Answer, AnswerOption


class AnswerOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerOption
        fields = '__all__'
        read_only_fields = ('answer',)  # ответ будет создан в самой сериализации


class AnswerSerializer(serializers.ModelSerializer):
    answer_items = AnswerOptionSerializer(many=True, required=False)

    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        answer_options = validated_data.pop('answer_options', [])  # получаем список ответов на вопросы
        answer = Answer.objects.create(**validated_data)
        if answer_options:
            # сохраняем все ответы пачкой
            AnswerOption.objects.bulk_create(
                AnswerOption(answer=answer, **item)
                for item in answer_options
            )
        return answer
