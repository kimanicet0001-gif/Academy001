from django.urls import path

from .views import (
    create_user,
    login_view,
    logout_view,
    dashboard
)

urlpatterns = [

    path(
        "register/",
        create_user,
        name="register"
    ),

    path(
        "login/",
        login_view,
        name="login"
    ),

    path(
        "logout/",
        logout_view,
        name="logout"
    ),

    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),
]