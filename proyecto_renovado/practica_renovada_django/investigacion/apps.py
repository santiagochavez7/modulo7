from django.apps import AppConfig

class InvestigacionConfig(AppConfig):
    # Cambiado de 'laboratorio' a 'investigacion' para coincidir con el nuevo nombre de la aplicación
    name = 'investigacion'
    verbose_name = 'Gestión de Investigaciones'
