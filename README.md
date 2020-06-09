Django Sweet Autocomplete
=====

The purpose of Sweet Autocomplete is to simplify autocomplete
functionalities implementation in your Django project.

Quick start
-----------

1. Add "sweetautocomplete" to your INSTALLED_APPS setting::
```python
INSTALLED_APPS = [
    ...
    'sweetautocomplete',
]
```

2. Include the autocomplete URLconf in your project `urls.py`:
```python
urlpatterns = [
    ...
    path("", include("sweetautocomplete.urls")),
    ...
]

```

3. Create a file called `autocomplete.py` in your app:
```python
from sweetautocomplete.autocomplete import autocompletefactory, AbstractAutocomplete
from .models import MyModel

class MyModelAutocomplete(AbstractAutocomplete):
    model = MyModel
    field = "field_name"

    class Serializer(serializers.ModelSerializer):
        label = serializers.CharField(source="field_name")

        class Meta:
            model = MyModel
            fields = ["label"]


autocompletefactory.register("model_name", MyModelAutocomplete)
```

4. Use autocomplete endpoints in your templates:
```html
"{% url 'autocomplete' 'model_name' %}?query=..."
```
