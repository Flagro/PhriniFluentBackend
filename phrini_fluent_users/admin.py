from django.contrib import admin
from .models import PhriniFluentUser

@admin.register(PhriniFluentUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telegram_handle', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'telegram_handle')
    list_filter = ('is_staff', 'is_active')
