from rest_framework_simplejwt.tokens import RefreshToken

from todo_api import models, exceptions, serializers


class LoginRegisterService:
    @staticmethod
    def register_user(data):
        name = data["name"]
        email = data["email"]
        password = data["password"]

        user_set = models.UserData.objects.filter(email=email)
        if user_set:
            raise exceptions.UserAlreadyExistsException

        user = models.UserData.objects.create(
            name=name,
            email=email,
        )
        user.set_password(password)
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

    @staticmethod
    def set_header(user, data):
        list_id = data.get("id", None)
        if not list_id:
            raise exceptions.MissingListIdException

        header_text = data.get("header", None)
        if not header_text:
            raise exceptions.MissingHeaderException

        try:
            list = models.List.objects.get(id=list_id, user=user)
        except models.List.DoesNotExist:
            raise exceptions.ListNotFoundException
        list.set_header(header_text)

    @staticmethod
    def get_lists(user):
        list_query_set = models.List.objects.filter(user=user)
        serializer = serializers.ListSerializer(list_query_set, many=True)
        return serializer.data
