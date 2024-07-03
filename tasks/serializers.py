from rest_framework import serializers
from .models import Task, Milestone


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'
