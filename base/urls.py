from django.contrib import admin
from django.urls import path
import base.views as base_views




urlpatterns = [
    path('', base_views.home_view, name='home'),
    path('about', base_views.about_view, name='about'),
    path('contact', base_views.contact_view, name='contact'),
    path('project', base_views.project_view, name='project'),
    path('services', base_views.services_view, name='services'),
]
