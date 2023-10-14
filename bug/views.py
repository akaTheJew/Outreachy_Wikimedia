"""
Module: views.py
Description: Defines views for the app1 application.
"""
from django.shortcuts import render

# Create your views here.
def home(request):
    """
    View for the home page.
    """
    return render(request, 'app1/templates/home.html')
