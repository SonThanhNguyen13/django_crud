from django.contrib import admin
from .models import DataTable
# Register your models here.


class DataTableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DataTable._meta.get_fields()]


admin.site.register(DataTable, DataTableAdmin)