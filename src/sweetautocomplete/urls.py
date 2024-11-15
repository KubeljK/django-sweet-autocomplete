from django.urls import re_path

from .views import AutoComplete


urlpatterns = [
    re_path(r"^autocomplete/(?P<model_name>[a-z_]+)$", AutoComplete.as_view(), name="autocomplete"),
]
