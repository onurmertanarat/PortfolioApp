from django.urls import path
from . import views

app_name = 'index_app'

urlpatterns = [
path('', views.index_app, name="index_app"),
path('projects/', views.projects, name="projects"),
path('contact/', views.contact_me, name="contact_me"),
]
