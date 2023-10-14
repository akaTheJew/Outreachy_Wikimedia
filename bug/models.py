"""
Module: models.py
Description: Defines the Image model.
"""

from django.db import models

# Create your models here.
class Image(models.Model):
    """
    Model representing an image.
    """
    photo = models.ImageField(upload_to='myimage')
    date = models.DateTimeField(auto_now_add = True)

# Final newline here
