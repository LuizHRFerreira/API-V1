from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ("id",)
    list_display = ("id", "email", "full_name", "is_staff", "is_active")
    search_fields = ("email", "full_name")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações pessoais", {"fields": ("full_name",)}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Datas importantes", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "full_name", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
