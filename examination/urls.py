from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_swagger.views import get_swagger_view

from . import views


router = DefaultRouter()
# router.register(r'exam', viewset=views.ExamModelViewSet, basename='Exam')

# schema_view = get_swagger_view(title='group', url='router.urls')

urlpatterns = [
    # path('', include(router.urls)),
    # path('list/', views.ExamListAPIView.as_view()),
    path('', views.ExamListAPIVIew.as_view()),
    path('question/', views.ExamQuestionAPIView.as_view()),
    path('question/answer', views.ExamQuestionCreateAPIView.as_view()),
    path('question/answer/<int:quiz_id>/<int:question_id>/<int:answer_id>', views.ExamQuestionView.as_view()),
]
