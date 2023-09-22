from rest_framework import serializers

from todo_api import models


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(min_length=8, max_length=100)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.List
        fields = ['id', 'header']
