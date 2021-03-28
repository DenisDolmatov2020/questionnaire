from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import ViewSet
from answer.models import Answer
from answer.serializers import AnswerSerializer


class AnswerViewSet(ViewSet):
    queryset = Answer.objects.all()
    serializer = AnswerSerializer

    # список всех пройденных опросов пользователя
    def list(self, request, *args):
        serializer = self.serializer(Answer.objects.filter(user=request.user), many=True)
        return Response(serializer.data)

    def create(self, request, *args):
        data_ = request.data.dict()
        data_['answer_options'] = json.loads(request.data.get('answer_options'))
        data_['user_id'] = request.user.id
        serializer = AnswerSerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
