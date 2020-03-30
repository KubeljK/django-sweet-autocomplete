=====
Django Sweet Autocomplete
=====

The purpose of Sweet Autocomplete is to simplify autocomplete
functionalities implementation in your Django project.

Quick start
-----------

1. Add "autocomplete" to your INSTALLED_APPS setting:

    INSTALLED_APPS = [
        ...
        'autocomplete',
    ]

2. Include the autocomplete URLconf in your project urls.py this:

    path('autocomplete/', include('autocomplete.urls')),

...

## How to use

Create a new file in your called `autocomplete.py`. Next, create an autocomplete model:

```python
from autocomplete import autocompletefactory, AbstractAutocomplete


class PoolsAutocomplete(AbstractAutocomplete):
    model = Pools
    field = "name"
    lookup = "__istartswith"

    class Serializer(serializers.ModelSerializer):
        label = serializers.CharField(source="name")

        class Meta:
            model = Municipality
            fields = ["label"]


autocompletefactory.register("pools", PoolsAutocomplete)
```

Next, register URLs:

```python
import autocomplete


urlpatterns = [

    ...

    # Autocomplete
    url(r"", include("autocomplete.urls"))
]

autocomplete.autodiscover()
```

Finally, in template you can call the following endpoint:
```html
"{% url 'autocomplete' 'pools' %}?query=..."
```
