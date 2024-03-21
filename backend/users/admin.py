from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # list_display 설정을 커스텀 모델에 맞게 수정합니다.
    list_display = ('email', 'store', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'store', 'groups')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    # add_fieldsets는 관리자 사이트에서 사용자를 생성할 때 사용되는 필드입니다.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'store', 'is_staff', 'is_active', 'groups')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
