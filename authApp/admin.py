from django.contrib import admin 
from authApp.models.product import Product
from authApp.models.check import Check
from authApp.models.user import User
from authApp.models.checkProduct import CheckProduct
from authApp.models.account import Account

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Check)
admin.site.register(CheckProduct)
admin.site.register(Account)