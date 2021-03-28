from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import ViewSet
from answer.models import Answer
from answer.serializers import AnswerSerializer
from question.models import Question


class AnswerViewSet(ViewSet):
    queryset = Answer.objects.all()
    serializer = AnswerSerializer

    # список всех пройденных опросов пользователя
    def list(self, request, *args):
        serializer = self.serializer(Answer.objects.filter(user=request.user), many=True)
        return Response(serializer.data)

    def create(self, request, *args):
        print(111111111111)
        answer_options = json.loads(request.data.get('answer_options'))
        answer_array = []
        print(2222222222)
        for index, answer_item in enumerate(answer_options):
            question = Question.objects.get(id=answer_item['question'])
            if question.type_answer == 'text':
                if isinstance(answer_item['text'], list):
                    answer_item['text'] = answer_item['text'][0]
                answer_array.append({'text': answer_item['text'], 'question': answer_item['question']})
            elif question.type_answer == 'single':
                if isinstance(answer_item['option'], list):
                    answer_item['option'] = answer_item['point'][0]
                answer_array.append({'option': int(answer_item['option']), 'question': answer_item['question']})
            if question.type_answer == 'multi':
                if not isinstance(answer_item['option'], list):
                    answer_item['option'] = answer_item['option'].split(',')
                for a in answer_item['option']:
                    answer_array.append({'option': int(a), 'question': answer_item['question']})
        data_ = request.data.dict()
        data_['answer_options'] = answer_array
        data_['user_id'] = request.user.id
        serializer = AnswerSerializer(data=data_)
        print('SERIALIZER DATA')
        print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.data)
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
