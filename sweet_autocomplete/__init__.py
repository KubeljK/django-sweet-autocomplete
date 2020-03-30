from django.utils.module_loading import autodiscover_modules

from sweet_autocomplete.autocomplete import autocompletefactory


def autodiscover():
    autodiscover_modules('autocomplete', register_to=autocompletefactory)


default_app_config = 'sweet_autocomplete.apps.SweetAutocompleteConfig'
