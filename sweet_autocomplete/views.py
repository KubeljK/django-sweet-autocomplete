import json

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.renderers import JSONRenderer

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

        query = request.query_params.get("query", "")
        extra_params = request.query_params.get("extra_params", None)
        if extra_params:
            extra_params = json.loads(extra_params)

        AutoCompleter = autocompletefactory.get(model_name)

        queryset = AutoCompleter.get_queryset(query, extra_params=extra_params)
        serializer = AutoCompleter.serialize(queryset)

        return Response(serializer.data, status.HTTP_200_OK)
