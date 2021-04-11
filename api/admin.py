from django.contrib import admin
from api.models import Account
# Register your models here.
@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = ["id" , "username" , "password" , "fullname"]
    admin.register(Account)