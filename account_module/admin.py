from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserManager(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'is_active', 'is_staff']
    list_editable = ['is_active', 'is_staff']