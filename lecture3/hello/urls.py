from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("name/<str:name>/", views.greet, name="greet")
]
