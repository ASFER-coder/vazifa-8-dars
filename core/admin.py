from django.contrib import admin, messages
from unfold.admin import ModelAdmin
from .models import Expense
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Expense)
class ExpenseAdmin(ModelAdmin):
    list_display = ["description", "amount", "category", 'created_at']
    list_filter = ('category', 'created_at')
    search_fields = ('description', 'category')
    actions = ['return_status']


@admin.action(description='Statusni return qilish')
def return_status(self, request, queryset):
    queryset.update(status='eski')
    messages.success(request, "Xarajatlar statusi 'eski' ga o'zgartirildi")