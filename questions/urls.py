from django.contrib import admin
from django.urls import path, include
from interview.views import InterviewList, InterviewCreate
from answer.views import AnswerViewSet

urlpatterns = [
    path('interviews/', InterviewList.as_view(), name='InterviewList'),
    path('answer/', AnswerViewSet.as_view({'get': 'list', 'post': 'create'}), name='AnswerViewSet'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
