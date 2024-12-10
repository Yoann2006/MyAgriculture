from django.apps import AppConfig


class MyagricultureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MYAGRICULTURE'

    def ready(self):
        import MYAGRICULTURE.signals