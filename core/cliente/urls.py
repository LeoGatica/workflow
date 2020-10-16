from django.urls import path
from .views import procesos


urlpatterns = [
    path('listaprocesos/',procesos, name="lista_procesos")


]

  
    
 