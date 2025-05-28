from django.contrib import admin
from main.models import Record, Category, Type, Status, SubCategory
# Register your models here.

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['data_created', 'type', 'category','subcategory', 'amount']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
        
@admin.register(Status, Type)
class StatusAndTypeAdmin(admin.ModelAdmin):
    list_display = ['name']