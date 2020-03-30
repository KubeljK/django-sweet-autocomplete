from rest_framework import serializers

from sweet_autocomplete.autocomplete import autocompletefactory, AbstractAutocomplete

from .models import City


class CityAutocomplete(AbstractAutocomplete):
    model = City
    field = "name"
    lookup = "__istartswith"

    class Serializer(serializers.ModelSerializer):
        label = serializers.CharField(source="name")

        class Meta:
            model = City
            fields = ["label"]


autocompletefactory.register("city", CityAutocomplete)
