# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("manageContract/", views.manageContract.as_view(), name="manageContract"),
]