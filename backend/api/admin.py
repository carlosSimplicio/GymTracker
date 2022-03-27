from django.contrib import admin
from api.models import MuscleGroup, Exercise, Session, Routine, Training, TrainingHistory

admin.site.register(MuscleGroup)
admin.site.register(Exercise)
admin.site.register(Session)
admin.site.register(Routine)
admin.site.register(Training)
admin.site.register(TrainingHistory)
