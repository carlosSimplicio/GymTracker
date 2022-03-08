from django.db import models

# Create your models here.

class MuscleGroup(models.Model):
  name=models.CharField(max_length=128)

class Exercise(models.Model):
  name=models.CharField(max_length=128)
  muscle_group=models.ForeignKey(MuscleGroup, related_name='exercises', on_delete=models.PROTECT)