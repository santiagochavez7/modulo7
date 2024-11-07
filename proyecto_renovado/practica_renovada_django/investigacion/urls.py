from django.urls import path
from . import vistas

urlpatterns = [
    path('', vistas.inicio, name='inicio'),
    path('lista/', vistas.LaboratorioListView.as_view(), name='lista_investigacion'),
    # Asegúrate de incluir todas tus rutas aquí
]
