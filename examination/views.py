from django.db.models import Sum, Q
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from quizzes.models import Question, Answer
from quizzes.serializers import QuestionSerializer
from .models import Examination, ExamQuestions
from .paginators import QuestionPagination
from .serializers import ExamSerializer, ExamQuestionSerializer


# class ExamListAPIView(generics.ListCreateAPIView):
#     serializer_class = ExamSerializer
#     queryset = Examination.objects.all()
#     # def get_queryset(self):
#     #     user = self.request.user
#     #     queryset = Examination.objects.filter(person=user, question_quiz=self.quiz)
#     #     return queryset
#     #
#     # def list(self, request, *args, **kwargs):
#     #     queryset = self.filter_queryset(self.get_queryset())
#     #
#     #     page = self.paginate_queryset(queryset)
#     #     if page is not None:
#     #         serializer = self.get_serializer(page, many=True)
#     #         return self.get_paginated_response(serializer.data)
#     #     serializer = self.get_serializer(queryset, many=True)
#     #     dicts = {
#     #         "data": serializer.data,
#     #         "total_grade": queryset.aggregate(Sum('grade'))
#     #     }
#     #     return Response(dicts)
#
# #
# # class ExamCreateAPIView(generics.CreateAPIView):
# #     serializer_class = ExamSerializer
# #     queryset = Examination.objects.all()
#
#
# class ExamModelViewSet(ModelViewSet):
#     serializer_class = ExamSerializer
#     queryset = Examination.objects.all()
#     pagination_class = QuestionPagination
#     permission_classes = [AllowAny, ]
#
#     # def perform_create(self, serializer):
#     #     return serializer.save(person=self.request.user)
#
#     def list(self, request, *args, **kwargs):
#         # queryset = self.filter_queryset(self.get_queryset())
#         get_queryset = Examination.objects.all()
#         queryset = self.filter_queryset(self.get_serializer)
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         dicts = {
#             "data": serializer.data,
#             "total_grade": queryset.aggregate(Sum('grade'))
#         }
#         return Response(dicts)
#
#     @action(detail=False, methods=['get'])
#     def search(self, request, pk=None):
#         queryset = self.queryset
#         name = request.query_params.get('name')
#         if name:
#             queryset = queryset.filter(
#                 Q(quiz__icontains=name) | Q(person__icontains=name))
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['get'])
#     def filters(self, request, pk=None):
#         queryset = self.queryset
#         group = request.query_params.get('quiz_group')
#         if group:
#             queryset = queryset.filter(group=group)
#         serializer = self.serializer_class(queryset, many=True)
#         print(group)
#         return Response(serializer.data)
#
#
# # class ExamView(generics.ListCreateAPIView):

class ExamListAPIVIew(generics.ListAPIView):
    serializer_class = ExamSerializer

    def get_queryset(self):
        # data = self.request.data.get('person')
        queryset = Examination.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(
                Q(person__icontains=name) | Q(surname__icontains=name) |
                Q(person__icontains=name)
            )
        return queryset


class ExamQuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = ExamQuestions.objects.all()


class ExamQuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = ExamQuestionSerializer
    queryset = ExamQuestions.objects.all()


class ExamQuestionView(generics.ListCreateAPIView):
    serializer_class = ExamQuestionSerializer

    def get_queryset(self):
        user = self.request.user
        quiz_id = self.kwargs.get('quiz_id')
        answer_id = self.kwargs.get('answer_id')
        question_id = self.kwargs.get('question_id')
        question = Question.objects.filter(id=question_id)
        answer = Answer.objects.filter(id=answer_id)
        imagine_number = 0
        if answer.correct_answer:
            if question.finish_time == 1:
                imagine_number = question.grade - (question.grade // question.question_time
                                                   * (question.grade // question.question_time))
                return imagine_number
            imagine_number = question.grade - (question.grade //
                                               question.question_time * question.finish_time)

            return imagine_number

        ExamQuestions.objects.create(
            person=user,
            quiz=quiz_id,
            question=question,
            answer=answer,
            grade=imagine_number
        )
