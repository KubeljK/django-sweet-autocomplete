from django.conf.urls import url

from autocomplete import views

urlpatterns = [
    url(r"^autocomplete/(?P<model_name>[a-z_]+)$", views.AutoComplete.as_view(), name="autocomplete"),
]
