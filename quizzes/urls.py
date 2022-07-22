from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_swagger.views import get_swagger_view

from . import views


router = DefaultRouter()
router.register(r'question', viewset=views.QuestionViewSet, basename='Question')
router.register(r'quiz', viewset=views.QuizViewSet, basename='quiz')
router.register(r'answers', viewset=views.AnswerViewSet, basename='Answers')


# schema_view = get_swagger_view(title='group', url='router.urls')

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(views.QuizListAPIView.as_view)),
    # path('detail/<int:pk>/', include(views.QuizRetrieveUpdateDestroyAPIView.as_view)),
]

