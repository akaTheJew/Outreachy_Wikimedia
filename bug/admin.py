"""
Module: admin.py
Description: Registers the Image model for use in the Django admin.
"""
from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Admin class for Image model.
    """
    list_display = ['id', 'photo', 'date']

# Final newline here
