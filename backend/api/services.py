from api.models import Exercise, MuscleGroup
from django.core import serializers


def list_musclegroups():
    musclegroups = MuscleGroup.objects.all()
    return [m.to_dict_json() for m in musclegroups]


def list_exercises():
    exercises = Exercise.objects.all()
    return [e.to_dict_json() for e in exercises]
