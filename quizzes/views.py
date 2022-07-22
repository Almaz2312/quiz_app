from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .models import Quiz, Question, Answer
from .paginators import QuestionPagination
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer
from .permissions import IsAdminOrReadOnly


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    pagination_class = QuestionPagination
    permission_classes = [AllowAny, ]


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny, ]
    pagination_class = QuestionPagination


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny, ]
