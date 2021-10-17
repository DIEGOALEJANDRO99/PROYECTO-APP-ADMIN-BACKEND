from django.contrib import admin 
from authApp.models.account import Account
from authApp.models.user import User

# Register your models here.
admin.site.register(User)
admin.site.register(Account)
