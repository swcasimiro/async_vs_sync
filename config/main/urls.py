from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('async/', views.async_main, name='async'),
    path('sync/', views.sync_main, name='sync')
]