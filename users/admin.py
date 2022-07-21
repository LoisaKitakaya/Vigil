from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(Address)
class AddressAdminView(admin.ModelAdmin):

    model = Address

    list_display = (
        'user',
        'city',
        'address',
        'phone_one',
        'phone_two',
    )

    list_filter = (
        'city',
    )