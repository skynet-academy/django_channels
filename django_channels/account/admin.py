from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Account
# Register your models here.

class AccountAdmin(UserAdmin):

    list_display = ('email', 'username', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
