from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DjanoAdmin
from .models import *

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(DjanoAdmin):
    model = User
    list_display = ("username",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2")},
        ),
    )
    ordering = ("username",)
    search_fields = ("username",)
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
