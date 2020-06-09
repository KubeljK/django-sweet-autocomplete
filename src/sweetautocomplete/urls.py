from django.conf.urls import url

from .views import AutoComplete


urlpatterns = [
    url(r"^autocomplete/(?P<model_name>[a-z_]+)$", AutoComplete.as_view(), name="autocomplete"),
]
