from rest_framework import serializers

from examination.models import Examination
from examination.serializers import ExamSerializer
from .models import Profile
# from examination.serializers import ExamSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    # exam = ExamSerializer

    class Meta:
        model = Profile
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super(UserProfileSerializer, self).to_representation(instance)
    #     if instance.examination.exists():
    #         representation['exam'] = ExamSerializer(instance.exam.all(),
    #                                                 many=True).data
