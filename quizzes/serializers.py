from rest_framework import serializers

from .models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ('question_quantity', 'user_quantity')

    def to_representation(self, instance):
        reps = super().to_representation(instance)
        reps['question_quantity'] = instance.question.all().count()
        if instance.question.exists():
            reps['question'] = QuestionSerializer(instance.question.all(),
                                                  many=True).data
        return reps


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(QuestionSerializer, self).to_representation(instance)
        if instance.answer.exists():
            representation['answers'] = AnswerSerializer(instance.answer.all(),
                                                         many=True).data
        else:
            representation['answers'] = []
        return representation


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class TestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'answer', 'answer_choice')