from rest_framework.view import exception_handler
from rest_framework.authtoken.views import ObtainAuthToken
from src.saccess_response.response import SaccessResponse


def saccess_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        data = response.data
        if not isinstance(data, dict):
            data = {'detail': data[list(data.keys())[0]][0]}
        response = SaccessResponse(data, saccess=False)
    else:
        response = SaccessResponse({'detail': 'Internal Server Error'}, saccess=False)
    return response


class SaccessObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return SaccessResponse(response.data)
