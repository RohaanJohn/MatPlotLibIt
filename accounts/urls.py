from django.urls import path
from . import views

urlpatterns = [path("my_view", views.ask, name="my_view")]    
