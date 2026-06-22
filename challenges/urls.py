from django.urls import path
from . import views

urlpatterns = [
    path("january", views.January),
    path("february", views.February)
]
