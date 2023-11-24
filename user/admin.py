from django.contrib import admin 
from user.models import user
@admin.register(user)


class useradmin(admin.ModelAdmin):
    list_display = ['username', 'fullname', 'id', 'phone_number']
    search_fields = ['id']