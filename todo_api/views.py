from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from todo_api import serializers, models, services, exceptions


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response_data = services.LoginRegisterService.register_user(serializer.validated_data)
        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response_data = services.LoginRegisterService.login_user(serializer.validated_data)
        return Response(response_data, status=status.HTTP_200_OK)


class CreateListView(APIView):
    def post(self, request):
        new_list_id = services.ListService.create_list(request.user)
        return Response({"id": new_list_id}, status=status.HTTP_201_CREATED)


class DeleteListView(APIView):
    def delete(self, request, id):
        services.ListService.delete_list(id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
