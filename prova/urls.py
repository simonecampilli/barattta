# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_persone, name='lista_persone'),
    path('aggiungi/', views.aggiungi_persona, name='aggiungi_persona'),

]
