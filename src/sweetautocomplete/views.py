import json

from rest_framework import status, views
from rest_framework.authentication import SessionAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .autocomplete import autocompletefactory


class AutoComplete(views.APIView):
    """
    Autocomplete endpoint.
    """

    renderer_classes = (JSONRenderer, )
    authentication_classes = (SessionAuthentication, )

    def get(self, request, model_name):
        """
        Filters Model instances and returns serialized QuerySet.
        """

        # Get parameters
        query = request.query_params.get("query", "")
        extra_params = request.query_params.get("extra_params", None)
        if extra_params:
            extra_params = json.loads(extra_params)

        AutoCompleter = autocompletefactory.get(model_name)

        result = AutoCompleter.get_result(query, extra_params=extra_params)

        return Response(result, status.HTTP_200_OK)
