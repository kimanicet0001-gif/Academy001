from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomLoginForm, CustomUserCreationForm
from .models import User
from django.contrib.auth.decorators import login_required


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

    context = {
        "form": form
    }

    return render(request, "users/create_user.html", context)
    return render(request, "users/create_user.html", {"form": form})


def users_list(request):

    users = User.objects.all()
    return render(request, "users/users_list.html", {"users": users})

    context = {
        "users": users
    }

    return render(request, "users/users_list.html", context)

def login_view(request):

    if request.method == "POST":

        form = CustomLoginForm(
            request,
            data=request.POST
        )

        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")

            password = form.cleaned_data.get("password")

            user = authenticate(
                request,
                username=username,
                password=password
            )

            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request, user)

                return redirect("dashboard")

    else:

        form = CustomLoginForm()

    context = {
        "form": form
    }
    return render(request, "users/login.html", {"form": form})

    return render(
        request,
        "users/login.html",
        context
    )

@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def dashboard(request):

    user = request.user

    context = {
        "user": user
    }

    return render(request, "users/dashboard.html", context)
    return render(request, "users/dashboard.html", {"user": request.user})