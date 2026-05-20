from django.test import TestCase
from django.urls import reverse

from .forms import CustomUserCreationForm
from .models import Department, University, User


class CustomUserCreationFormTests(TestCase):
    def setUp(self):
        self.university_a = University.objects.create(name="Alpha University")
        self.university_b = University.objects.create(name="Beta University")
        self.department_a = Department.objects.create(
            name="Computer Science", university=self.university_a
        )

    def test_reject_department_from_another_university(self):
        form = CustomUserCreationForm(
            data={
                "username": "user1",
                "first_name": "User",
                "last_name": "One",
                "email": "user1@example.com",
                "role": "delegate",
                "university": self.university_b.id,
                "department": self.department_a.id,
                "phone_number": "123456",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("department", form.errors)


class UsersViewsTests(TestCase):
    def setUp(self):
        self.university = University.objects.create(name="Gamma University")
        self.department = Department.objects.create(
            name="Mathematics", university=self.university
        )
        self.user = User.objects.create_user(
            username="john",
            password="StrongPass123!",
            role="delegate",
            university=self.university,
            department=self.department,
        )

    def test_login_success_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("login"), {"username": "john", "password": "StrongPass123!"}
        )
        self.assertRedirects(response, reverse("dashboard"))

    def test_dashboard_requires_authentication(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_users_list_page_loads(self):
        response = self.client.get(reverse("users_list"))
        self.assertEqual(response.status_code, 200)
