from rest_framework_simplejwt.tokens import RefreshToken

from todo_api import models, exceptions


class LoginRegisterService:
    @staticmethod
    def register_user(data):
        user = models.UserData.objects.create(
            name=data["name"],
            email=data["email"],
        )

        user.set_password(data["password"])
        user.save()

        refresh = RefreshToken.for_user(user)
        response_data = {
            "token": str(refresh.access_token),
            "name": user.name,
            "email": user.email,
        }

        return response_data

    @staticmethod
    def login_user(data):
        email = data["email"]
        password = data["password"]
        try:
            user = models.UserData.objects.get(email=email)
        except models.UserData.DoesNotExist:
            raise exceptions.IncorrectEmailException

        if not user.check_password(password):
            raise exceptions.IncorrectPasswordException

        refresh = RefreshToken.for_user(user)
        response_data = {
            "token": str(refresh.access_token),
            "name": user.name,
            "email": user.email,
        }

        return response_data


class ListService:
    @staticmethod
    def create_list(user):
        new_list = models.List.objects.create(user=user)
        return new_list.id

    @staticmethod
    def delete_list(id, user):
        try:
            list = models.List.objects.get(id=id, user=user)
        except models.List.DoesNotExist:
            raise exceptions.ListNotFoundException
        list.delete()
