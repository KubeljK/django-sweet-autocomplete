from django.test import TestCase

from smartautocomplete import autocompletefactory
from smartautocomplete_tests.autocomplete import InvalidAutocomplete, InvalidSimpleBasicAutocomplete


class AutoCompleteFactoryTestCase(TestCase):
    def test_invalid_register(self):
        """Trying to register an invalid Autocompleter should raise an error."""

        # This should fail.
        with self.assertRaises(TypeError):
            autocompletefactory.register("invalid", InvalidAutocomplete)


class AutoCompleteInheritanceTestCase(TestCase):
    def test_invalid_autocompleter(self):
        """Test if get_result correctly raises error if not implemented."""

        with self.assertRaises(NotImplementedError):
            _ = InvalidSimpleBasicAutocomplete.get_result()
