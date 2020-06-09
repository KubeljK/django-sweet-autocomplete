from django.utils.module_loading import autodiscover_modules

from .autocomplete import autocompletefactory


default_app_config = 'sweetautocomplete.apps.SweetAutocompleteConfig'


def autodiscover():
    autodiscover_modules('autocomplete', register_to=autocompletefactory)
