from django.test import TestCase

from smartautocomplete_tests.models import SimpleModel


class AutoCompleteTestCase(TestCase):
    def test_simple_basic_autocompleter(self):
        """Test if SimpleBasicAutocomplete works correctly."""

        response = self.client.get("/autocomplete/simplebasic")
        self.assertEqual(response.json(), [{"label": "label1"}])

        response = self.client.get("/autocomplete/simplebasic?query=unimportant")
        self.assertEqual(response.json(), [{"label": "label1"}])

    def test_simple_model_autocompleter(self):
        """Test if SimpleModelAutocomplete works correctly."""

        items = [
            SimpleModel(**{"text": "First item"}),
            SimpleModel(**{"text": "Second item"})
        ]
        SimpleModel.objects.bulk_create(items)

        # Return all items
        response = self.client.get("/autocomplete/simplemodel")
        self.assertEqual(
            response.json(),
            [{"label": "First item"}, {"label": "Second item"}]
        )

        # Return filtered items
        response = self.client.get("/autocomplete/simplemodel?query=First")
        self.assertEqual(
            response.json(),
            [{"label": "First item"}]
        )
