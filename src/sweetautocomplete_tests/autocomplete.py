from rest_framework import serializers

from sweetautocomplete import autocompletefactory
from sweetautocomplete.autocomplete import AbstractAutocomplete, ModelAutocomplete
from .models import SimpleModel


class InvalidAutocomplete():
    """Registring this autocomplete should raise an Exception."""
    def __init__(self, *args, **kwargs):
        pass


class InvalidSimpleBasicAutocomplete(AbstractAutocomplete):
    """Using this autocomplete should raise NotImplementedError."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SimpleBasicAutocomplete(AbstractAutocomplete):

    def get_result(*args, **kwargs):
        return [{"label": "label1"}]


class SimpleModelAutocomplete(ModelAutocomplete):
    model = SimpleModel
    field = "text"
    lookup = "__istartswith"

    class Serializer(serializers.ModelSerializer):
        label = serializers.CharField(source="text")

        class Meta:
            model = SimpleModel
            fields = ["label"]


autocompletefactory.register("simplemodel", SimpleModelAutocomplete)
autocompletefactory.register("simplebasic", SimpleBasicAutocomplete)
