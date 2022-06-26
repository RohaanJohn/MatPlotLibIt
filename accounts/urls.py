from django.urls import path
from . import views

urlpatterns = [path("register", views.register, name="register"), path("login", views.login, name="login"), path("logout", views.logout, name="logout"),  path("trashdetection", views.trashdetection, name="trashdetection"), path("contact", views.contact, name="contact"), path("trashorclean", views.trashorclean, name="trashorclean")]    
