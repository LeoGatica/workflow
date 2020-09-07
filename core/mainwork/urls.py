from django.urls import path
from .views import index, logged_in

urlpatterns = [
    path('', index, name="index"),
    path('logged_in/', logged_in),


    
]
