from django.contrib.auth.models import User
from django.db import models


class MuscleGroup(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return dict(
            id=self.id,
            name=self.name,
        )


class Exercise(models.Model):
    name = models.CharField(max_length=128)
    muscle_group = models.ForeignKey(
        MuscleGroup, related_name="+", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return dict(
            id=self.id,
            name=self.name,
            musclegroup=self.muscle_group.to_dict_json(),
        )


class Session(models.Model):
    exercise = models.ForeignKey(Exercise, related_name="+", on_delete=models.PROTECT)
    reps = models.IntegerField()
    load = models.FloatField()

    def __str__(self):
        return f"{self.exercise.name} - {self.reps} X {self.load}"


class Routine(models.Model):
    sessions = models.ManyToManyField(Session, related_name="+")
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class RoutineSessionHistory(models.Model):
    routine = models.ForeignKey(Routine, related_name="+", on_delete=models.PROTECT)
    session = models.ForeignKey(Session, related_name="+", on_delete=models.PROTECT)
    reps = models.IntegerField()
    load = models.FloatField()
