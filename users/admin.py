from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, NewsletterSubscription

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdminView(admin.ModelAdmin):

    model = NewsletterSubscription

    list_display = (
        'user',
        'email',
    )

    list_filter = (
        'created_date',
        'updated_date',
    )