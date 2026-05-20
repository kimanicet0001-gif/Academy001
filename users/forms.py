from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Department, User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "university",
            "department",
            "phone_number",
        )

    def clean(self):
        cleaned_data = super().clean()
        university = cleaned_data.get("university")
        department = cleaned_data.get("department")

        if department and university and department.university_id != university.id:
            self.add_error(
                "department",
                "The selected department does not belong to the selected university.",
            )

        return cleaned_data


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.setdefault("autocomplete", "username")
        self.fields["password"].widget.attrs.setdefault("autocomplete", "current-password")
