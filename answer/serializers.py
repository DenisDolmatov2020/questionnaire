from rest_framework import serializers
from answer.models import Answer, AnswerOption

from question.models import QuestionOption


class AnswerOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerOption
        fields = '__all__'
        read_only_fields = ('answer',)  # ответ будет создан в самой сериализации


class AnswerSerializer(serializers.ModelSerializer):
    answer_options = AnswerOptionSerializer(many=True, required=False)

    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        answer_options = validated_data.pop('answer_options', [])  # получаем список ответов на вопросы
        answer = Answer.objects.create(**validated_data)
        if answer_options:
            answer_array = []
            for index, answer_item in enumerate(answer_options):
                question = answer_item['question']
                if question.type_answer == 'single':
                    answer_item['option_id'] = int(answer_item['text'])
                    answer_item['text'] = ''
                elif question.type_answer == 'multi':
                    del answer_options[index]
                    options = answer_item['text'].split(',')
                    answer_item['text'] = ''
                    for option in options:
                        answer_item['option_id'] = int(option)
                        answer_array.append(answer_item)
            # сохраняем все ответы пачкой
            AnswerOption.objects.bulk_create(
                AnswerOption(answer=answer, **item)
                for item in answer_options + answer_array
            )
        return answer
