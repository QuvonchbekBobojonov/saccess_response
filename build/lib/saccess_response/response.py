from rest_framework.response import Response
from rest_framework import status as drf_status


class SaccessResponse(Response):
    def __init__(self, data=None, headers=None, exception=False, content_type=None, saccess=True):
        data = {'saccess': saccess, 'result': data}
        status = drf_status.HTTP_200_OK
        super().__init__(data, status, headers, exception, content_type)
