from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("", include("sweetautocomplete.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
]
