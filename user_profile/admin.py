from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


class UserInline(admin.TabularInline):
    model = Profile


class ProfileAdmin(admin.ModelAdmin):
    inlines = [UserInline]


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
