from rest_framework import serializers
from .models import *


class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = ('id', 'name', 'city', 'start', 'end', 'university', 'acronym', 'type')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'type')


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('id', 'name', 'type')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'name', 'city', 'start', 'end', 'university')


class EducationNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationNote
        fields = ('id', 'education', 'item')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'city', 'start', 'end', 'place', 'personal')


class ProjectNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectNote
        fields = ('id', 'project', 'item')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'city', 'start', 'end', 'company', 'volunteer')


class WorkNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationNote
        fields = ('id', 'work', 'item')
