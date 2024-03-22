from django.urls import path
from . import views

urlpatterns = [
    path("get-csrf-token/", views.get_csrf_token, name="get_csrf_token"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user , name="logout_user"),
    path("register/", views.register_user, name="register_user"),
    path("activate_account/<uidb64>/<token>/", views.activate_account, name="activate_account"),
]