from django.contrib import admin

from .models import Profile, Transaction, Stock

# Register your models here.

admin.site.register(Profile)
admin.site.register(Transaction)
admin.site.register(Stock)