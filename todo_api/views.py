from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from todo_api import serializers, models

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
            return Response({
                "error": ["Incorrect email"]
            }, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({
                "error": ["Incorrect password"]
            }, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        data = {
            "token": str(refresh.access_token),
            "name": user.name,
            "email": user.email,
        }
        return Response(data, status=status.HTTP_200_OK)


class CreateListView(APIView):
    def post(self, request):
        user = request.user
        new_list = models.List.objects.create(user=user)
        return Response({"id": new_list.id}, status=status.HTTP_201_CREATED)


class DeleteListView(APIView):
    def delete(self, request):
        user = request.user
        list_id = request.data.get("id", None)
        if not list_id:
            return Response({"error": ["Missing list id"]}, status=status.HTTP_400_BAD_REQUEST)

        list_set = models.List.objects.filter(id=list_id, user=user)
        if not list_set:
            return Response({"error": ["List not found"]}, status=status.HTTP_404_NOT_FOUND)

        list_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
