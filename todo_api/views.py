from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from todo_api import serializers, models, services, exceptions


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = models.UserData.objects.create(
            name=serializer.validated_data["name"],
            email=serializer.validated_data["email"],
        )

        user.set_password(serializer.validated_data["password"])
        user.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "token": str(refresh.access_token),
            "name": user.name,
            "email": user.email,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        try:
            user = models.UserData.objects.get(email=email)
        except models.UserData.DoesNotExist:
            raise exceptions.IncorrectEmailException

        if not user.check_password(password):
            raise exceptions.IncorrectPasswordException

        refresh = RefreshToken.for_user(user)
        data = {
            "token": str(refresh.access_token),
            "name": user.name,
            "email": user.email,
        }
        return Response(data, status=status.HTTP_200_OK)


class CreateListView(APIView):
    def post(self, request):
        new_list_id = services.ListService.create_list(request.user)
        return Response({"id": new_list_id}, status=status.HTTP_201_CREATED)


class DeleteListView(APIView):
    def delete(self, request, id):
        services.ListService.delete_list(id, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
