from rest_framework import serializers
from django.contrib.auth import get_user_model

# from quizzes.models import Answer, Question, Quiz
from quizzes.models import Answer, Question
from .models import Examination, ExamQuestions
from quizzes.serializers import QuestionSerializer, AnswerSerializer

User = get_user_model()


class ExamQuestionSerializer(serializers.ModelSerializer):
    # exam_answers = AnswerSerializer

    class Meta:
        model = ExamQuestions
        fields = '__all__'
        read_only_fields = ('person', 'quiz', 'grade')


class ExamSerializer(serializers.ModelSerializer):
    questions_exam = ExamQuestionSerializer

    class Meta:
        model = Examination
        exclude = ('grade',)