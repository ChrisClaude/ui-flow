from rest_framework import serializers
from .models import User, Project, ProjectMember


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(required=True, max_length=200)
    email = serializers.CharField(required=True, max_length=200)
    password = serializers.CharField(required=True, max_length=200)

    def create(self, validated_data):
        """
        Create and return a new 'User' instance, given the validated data
        :param validated_data:
        :return: a new 'User' instance, given the validated data
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'User' instance, given the validated data
        :param instance:
        :param validated_data:
        :return: an existing 'User' instance, given the validated data
        """
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'label', 'timestamp', 'project_creator']


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['id', 'project', 'project_member']

