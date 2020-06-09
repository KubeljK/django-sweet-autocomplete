from rest_framework import serializers

from sweetautocomplete.autocomplete import autocompletefactory, ModelAutocomplete

from .models import City


class CityAutocomplete(ModelAutocomplete):
    model = City
    field = "name"
    lookup = "__istartswith"

    class Serializer(serializers.ModelSerializer):
        label = serializers.CharField(source="name")

        class Meta:
            model = City
            fields = ["label"]


autocompletefactory.register("city", CityAutocomplete)
