from rest_framework.exceptions import ValidationError
from rest_framework import status as drf_status


class SaccessValidationError(ValidationError):
    # Override the default status code to always return HTTP 200 OK for this exception.
    status_code = drf_status.HTTP_200_OK

    def __init__(self, detail=None, code=None, saccess=False):
        # Customize the detail structure to include the 'saccess' key along with the error result.
        detail = {'saccess': saccess, 'result': detail}
        super().__init__(detail, code)
