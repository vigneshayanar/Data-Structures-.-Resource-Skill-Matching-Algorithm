from rest_framework import serializers
from .models import Skill,Resource,Project,TaskAssignments,Task

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'

class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resource
        fields='__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

class TaskassignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskAssignments
        fields='__all__'