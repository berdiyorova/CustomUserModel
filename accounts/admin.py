from django.contrib import admin
from django.contrib.auth import get_user_model

user_model = get_user_model()


@admin.register(user_model)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'is_active', 'created_at',)
    list_filter = ('is_active', 'created_at',)
    search_fields = ('email', 'full_name')
