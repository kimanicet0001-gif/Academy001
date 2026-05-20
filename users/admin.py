from django.contrib import admin

from .models import Department, University, User


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "university", "created_at")
    list_filter = ("university",)
    search_fields = ("name", "university__name")
    ordering = ("university__name", "name")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "role", "university", "department")
    list_filter = ("role", "university", "department")
    search_fields = ("username", "first_name", "last_name", "email")
