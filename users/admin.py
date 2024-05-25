from django.contrib import admin

from users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'birth_date', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'phone')
