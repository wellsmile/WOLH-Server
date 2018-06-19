from django.contrib import admin
from .models import Items, Operation

# Register your models here.
@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'descript', 'type', 'info')
    
@admin.register(Operation)
class OperationsAdmin(admin.ModelAdmin):
    list_display=('id', 'time', 'user', 'operation', 'info')