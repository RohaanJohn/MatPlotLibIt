from django.urls import path
from . import views

urlpatterns = [path("matplotlibit", views.matplotlibit, name="matplotlibit")]    
