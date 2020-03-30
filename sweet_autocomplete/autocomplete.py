from abc import ABC


class AbstractAutocomplete(ABC):

    @classmethod
    def get_queryset(cls, query, extra_params=None, unique=True):
        filters = {
            f"{cls.field}{cls.lookup}": query
        }
        if extra_params:
            filters.update(cls.extra_params_to_filters(extra_params))

        qs = cls.model.objects.filter(**filters).order_by(cls.field)
        if unique:
            qs = qs.distinct(cls.field)
        return qs[:20]

    @classmethod
    def serialize(cls, qs):
        return cls.Serializer(qs, many=True)

    @classmethod
    def extra_params_to_filters(extra_params):
        pass


class AutoCompleteFactory:

    def __init__(self):
        self._models_registry = {}

    def get(self, model_name):
        return self._models_registry.get(model_name)

    def register(self, name, model):
        if not issubclass(model, AbstractAutocomplete):
            raise TypeError("Supplied model is not a valid model.")

        self._models_registry[name] = model


autocompletefactory = AutoCompleteFactory()
