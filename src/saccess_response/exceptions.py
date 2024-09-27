from rest_framework.exceptions import ValidationError
from rest_framework import status as drf_status


class SaccessValidationError(ValidationError):
    status_code = df_status.HTTP_200_OK

    def __init__(self, detail=None, code=None, saccess=False):
        detail = {'saccess': saccess, 'result': detail}
        super().__init__(detail, code)