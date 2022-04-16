from django.contrib import admin
from .models import NamingSeries, MainUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    ordering = ('-create_date',)
    search_fields = ('user_name', 'email')
    list_display = ('user_name', 'email', 'create_date',
                    'is_active', 'is_manager', 'is_superuser',
                    'is_staff',)
    fieldsets = (
        (None, {'fields': ('user_name', 'email',)}),
        ('Permissions',
            {'fields': (
                'is_staff','is_active','is_manager',
                'is_superuser','groups', 'user_permissions'
                )
            }
        ),
    )
    add_fieldsets = (
        (None, {
             'classes': ('wide',),
             'fields': ('user_name', 'email', 'create_date',
                    'is_active', 'is_manager', 'is_superuser',
                    'is_staff','groups', 'user_permissions')
         }),
    )

admin.site.register(NamingSeries)
admin.site.register(MainUser, UserAdminConfig)
