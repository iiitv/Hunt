from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
    def ready(self):
        from api import scheduler
        scheduler.start_job()
        print("Started")
