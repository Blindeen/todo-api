from todo_api import models, exceptions


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
