from django.contrib import admin
from django.urls import path, include
from interview.views import InterviewList
from answer.views import InterviewUserViewSet

urlpatterns = [
    path('interview/', InterviewList.as_view(), name='InterviewList'),
    path(
        'interview-user/', InterviewUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='InterviewUserViewSet'
    ),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
