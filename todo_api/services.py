from todo_api import models

class ListService:
    @staticmethod
    def create_list(user):
        new_list = models.List.objects.create(user=user)
        return new_list.id

    @staticmethod
    def delete_list(id, user):
        list_set = models.List.objects.filter(id=id, user=user)
        if not list_set:
            return False

        list_set.delete()
        return True
