from django.contrib.auth.models import User
from django.db import models

#
class MuscleGroup(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return dict(
            id=self.id,
            name=self.name,
            musclegroup=self.muscle_group.to_dict_json(),
        )

class Session(models.Model):
    reps = models.IntegerField()
    load = models.FloatField()
    rest = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reps} X {self.load} X {self.rest} seg"

    def to_dict_json(self):
        return dict(
            id=self.id,
            repetitions=self.reps,
            load=self.load,
            rest=self.rest,
            order=self.order,
        )


class Routine(models.Model):
    exercise = models.ForeignKey(Exercise, related_name="+", on_delete=models.PROTECT)
    sessions = models.ManyToManyField(Session, related_name="routine")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.exercise.name} - {self.sessions.all().count()} Séries'
    
    def to_dict_json(self):
        return dict(
            id=self.id,
            exercise=self.exercise.to_dict_json(),
            sessions=[s.to_dict_json() for s in self.sessions.all()]
        )

class Training(models.Model):
    routines=models.ManyToManyField(Routine)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return dict(
            id=self.id,
            name=self.name,
            routines=[s.to_dict_json() for s in self.routines.all()]
        )


class TrainingHistory(models.Model):
    train=models.ForeignKey(Training, related_name="+", on_delete=models.PROTECT)
    routine = models.ForeignKey(Routine, related_name="+", on_delete=models.PROTECT)
    session = models.ForeignKey(Session, related_name="+", on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name="+", on_delete=models.PROTECT)
    reps = models.IntegerField()
    load = models.FloatField()
    rest = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)