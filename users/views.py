from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomLoginForm, CustomUserCreationForm
from .models import User


def home(request):
    return render(request, "users/home.html")


def create_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users_list")
    else:
        form = CustomUserCreationForm()

    return render(request, "users/create_user.html", {"form": form})


def users_list(request):
    users = User.objects.select_related("university", "department").all()
    return render(request, "users/users_list.html", {"users": users})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = CustomLoginForm(request)

    return render(request, "users/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    return render(request, "users/dashboard.html", {"user": request.user})
