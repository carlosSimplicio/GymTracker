from api import views
from django.urls import path

urlpatterns = [
    path("musclegroup/list", views.list_musclegroups),
    path("exercise/list", views.list_exercises),
    path("trainings/list", views.list_trainings),
]
