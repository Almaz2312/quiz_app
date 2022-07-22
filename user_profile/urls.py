from django.urls import path

from . import views


urlpatterns = [
    path('', views.UserProfileListView.as_view()),
    path('profile/<int:pk>/', views.UserProfileCreateView.as_view()),
]
