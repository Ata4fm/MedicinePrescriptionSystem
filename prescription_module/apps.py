from django.apps import AppConfig


class PrescriptionModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prescription_module'

    verbose_name = 'ماژول نسخه دارو'
