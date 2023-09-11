from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
