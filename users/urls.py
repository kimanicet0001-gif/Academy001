from django.urls import path

from .views import create_user, dashboard, login_view, logout_view, users_list

urlpatterns = [
    path("register/", create_user, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("list/", users_list, name="users_list"),
]
