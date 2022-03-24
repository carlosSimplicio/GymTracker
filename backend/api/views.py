from http import HTTPStatus
from django.forms import ValidationError
from django.http import HttpResponse, JsonResponse
from api import services


def list_musclegroups(_):
    try:
        musclegroups = services.list_musclegroups()
        return JsonResponse(musclegroups, status=HTTPStatus.OK, safe=False)
    except ValidationError as e:
        return HttpResponse(e.__str__, status=HTTPStatus.BAD_REQUEST)


def list_exercises(_):
    try:
        exercises = services.list_exercises()
        return JsonResponse(exercises, status=HTTPStatus.OK, safe=False)
    except ValidationError as e:
        return HttpResponse(e.__str__, status=HTTPStatus.BAD_REQUEST)


def list_routines(_):
    return JsonResponse({})
