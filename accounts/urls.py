from django.urls import path
from . import views

urlpatterns = [path("ask", views.verify, name="ask")]    
