from rest_framework.views import exception_handler
from rest_framework.authtoken.views import ObtainAuthToken
from .response import SaccessResponse


# Custom exception handler that uses the default DRF exception handler,
# but wraps the response in a SaccessResponse for consistent formatting.
def saccess_exception_handler(exc, context):
    # Call the default exception handler to get the standard response.
    response = exception_handler(exc, context)

    if response is not None:
        data = response.data

        # Ensure the response data is a dictionary. If not, format it as expected.
        if not isinstance(data, dict):
            # Extract the first error message and wrap it in a 'detail' key.
            data = {'detail': data[list(data.keys())[0]][0]}

        # Return the error wrapped in a SaccessResponse, with `saccess=False` indicating failure.
        response = SaccessResponse(data, saccess=False)
    else:
        # If no response, provide a generic internal server error message.
        response = SaccessResponse({'detail': 'Internal Server Error'}, saccess=False)

    return response


# Custom authentication view that uses the ObtainAuthToken view,
# but wraps the token response in a SaccessResponse for consistent formatting.
class SaccessObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Call the standard ObtainAuthToken post method to get the token response.
        response = super().post(request, *args, **kwargs)

        # Wrap the response data (usually the token) in a SaccessResponse.
        return SaccessResponse(response.data)
