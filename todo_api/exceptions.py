from rest_framework.exceptions import APIException

class IncorrectEmailException(APIException):
    status_code = 400
    default_detail = {"Credentials": ["Incorrect email."]}


class IncorrectPasswordException(APIException):
    status_code = 400
    default_detail = {"Credentials": ["Incorrect password."]}


class ListNotFoundException(APIException):
    status_code = 404
    default_detail = {"Resources": ["List not found."]}


class MissingListIdException(APIException):
    status_code = 400
    default_detail = {"Body": ["Missing list id."]}


class MissingHeaderException(APIException):
    status_code = 400
    default_detail = {"Body": ["Missing header id"]}
