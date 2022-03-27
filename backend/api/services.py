from api.models import Exercise, MuscleGroup, Training


def list_musclegroups():
    musclegroups = MuscleGroup.objects.all()
    return [m.to_dict_json() for m in musclegroups]


def list_exercises():
    exercises = Exercise.objects.select_related("muscle_group").all()
    return [e.to_dict_json() for e in exercises]

def list_trainings():
    trainings = Training.objects.prefetch_related('routines__sessions').all()
    return [t.to_dict_json() for t in trainings]