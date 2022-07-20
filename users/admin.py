from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserAddress

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(UserAddress)
class UserAddressAdminView(admin.ModelAdmin):

    model = UserAddress

    list_display = (
        'user',
        'city',
        'address_one',
        'primary_phone',
    )

    list_filter = (
        'city',
    )