from django.shortcuts import render
from rest_framework import generics

from user_profile.models import Profile
from user_profile.permissions import IsAuthorOrReadOnly
from user_profile.serializers import UserProfileSerializer


class UserProfileListView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class UserProfileCreateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthorOrReadOnly, ]
