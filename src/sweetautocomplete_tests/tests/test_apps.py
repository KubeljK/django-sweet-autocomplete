from django.test import TestCase

from sweetautocomplete import autocompletefactory


class RegistryInitTestCase(TestCase):
    def test_correctly_initialized(self):
        """Test if autodiscovering and registring works correctly."""

        AutoCompleter = autocompletefactory.get("simplemodel")
        self.assertIsNotNone(AutoCompleter)

        # Unexisting model
        AutoCompleter = autocompletefactory.get("nonexistingmodel")
        self.assertIsNone(AutoCompleter)
