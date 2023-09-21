from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Account

class AccountAdmin(UserAdmin):

    list_display = ['email' , 'first_name' , "last_name" , 'username' , "joined_date", 'last_login']
    list_display_links =['email' , 'first_name' , "last_name" , 'username' ,]
    readonly_fields = ['joined_date' , 'last_login']

    ordering = ['-joined_date']

    filter_horizontal = ()
    list_filter =()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)