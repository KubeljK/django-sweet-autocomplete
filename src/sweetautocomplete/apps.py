from django.apps import AppConfig


class SweetAutocompleteConfig(AppConfig):
    name = 'sweetautocomplete'

    def ready(self):
        super().ready()
        self.module.autodiscover()
