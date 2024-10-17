from rest_framework.response import Response
from rest_framework import status as drf_status


# Custom response class that standardizes API responses with an additional
# 'saccess' field, indicating success or failure, and a 'result' field holding the actual data.
class SaccessResponse(Response):
    def __init__(self, data=None, headers=None, exception=False, content_type=None, saccess=True):
        # Wrap the data in a standardized format with 'saccess' indicating success status,
        # and 'result' containing the response payload.
        data = {'saccess': saccess, 'result': data}

        # Default the status code to 200 (OK) unless otherwise specified.
        status = drf_status.HTTP_200_OK

        # Call the parent class constructor to build the response with the given data.
        super().__init__(data, status, headers, exception, content_type)
