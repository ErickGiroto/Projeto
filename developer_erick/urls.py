from django.urls import path
from developer_erick.views import home, sobre, contato


urlpatterns = [
    
    #dominio.com/developer_erick/home
    path('', home), #HOME
    
    #dominio.com/developer_erick/sobre
    path('sobre/',sobre), #SOBRE
    
    #dominio.com/developer_erick/contato
    path('contato/',contato), #CONTATO
    
]
