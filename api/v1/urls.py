from api.v1.viewsets import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('questions/', QuestionsList.as_view(), name='questions_list'),
    path('questions/<int:pk>/', QuestionsDetail.as_view(), name='question_detail'),
    path('questions/<int:pk>/answers/',
         QuestionAnswerDetail.as_view({'get': 'answers'}), name='answers_for_question'),
    path('questions/answers/', AnswersList.as_view(), name='answers_list'),
    path('questions/answers/<int:pk>/',
         AnswersDetail.as_view(), name='answer_detail')
]
