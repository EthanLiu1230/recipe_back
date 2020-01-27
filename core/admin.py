from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# support for translation
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        # section
        (
            None,  # title
            {'fields': ('email', 'password'), }
        ),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser'), }
        ),
        (
            _('Important dates'),
            {'fields': ('last_login',)}
        ),
    )

    # add edit page
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            },
        )
    )


admin.site.register(models.User, UserAdmin)
