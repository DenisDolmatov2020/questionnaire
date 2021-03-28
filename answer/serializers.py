from rest_framework import serializers
from answer.models import Answer, AnswerOption, AnswerOptionItem
from question.serializers import QuestionOptionSerializer


class AnswerOptionItemSerializer(serializers.ModelSerializer):
    question_option = serializers.StringRelatedField()

    class Meta:
        model = AnswerOptionItem
        fields = ('question_option',)


class AnswerOptionSerializer(serializers.ModelSerializer):
    answer_option_item = AnswerOptionItemSerializer(many=True, required=False)

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
            for index, answer_item in enumerate(answer_options):
                question = answer_item['question']
                if question.type_answer == 'single':
                    answer_item['option_id'] = int(answer_item['text'])
                    answer_item['text'] = ''
                elif question.type_answer == 'multi':
                    del answer_options[index]
                    answer_options = answer_item['text'].split(',')
                    answer_item['text'] = ''
                    answer_option = AnswerOption.objects.create(answer=answer, **answer_item)
                    for option in answer_options:
                        AnswerOptionItem.objects.create(
                            question_option_id=option, answer_option=answer_option
                        )

                        # multi_answers.append(answer_item)

            # сохраняем все ответы пачкой
            '''AnswerOption.objects.bulk_create(
                AnswerOption(answer=answer, **item)
                for item in answer_options + multi_answers
            )'''
        return answer
