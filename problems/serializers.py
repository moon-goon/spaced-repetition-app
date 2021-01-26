from rest_framework import serializers
from problems.models import Problem

class ProblemSerializer(serializers.Serializer):
    class Meta:
        model = Problem
        fields = '__all__'
