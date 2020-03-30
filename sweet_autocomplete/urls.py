from django.conf.urls import url

from .views import AutoCompleteView


urlpatterns = [
    url(r"^autocomplete/(?P<model_name>[a-z_]+)$", AutoCompleteView.as_view(), name="autocomplete"),
]
