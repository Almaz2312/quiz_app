from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

from .models import Group
from .serializers import GroupSerializer
from .permissions import IsAdminOrReadOnly


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly, ]

