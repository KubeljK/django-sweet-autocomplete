from django.apps import AppConfig


class SweetAutocompleteConfig(AppConfig):
    name = 'sweet_autocomplete'
    
    def ready(self):
        super().ready()
        self.module.autodiscover()
