from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from .response import SaccessResponse


# Custom CreateModelMixin to wrap the response in SaccessResponse after creating a new object.
class SaccessCreateModelMixin(CreateModelMixin):
    def create(self, request, *args, **kwargs):
        # Call the default create method and get the standard response.
        response = super().create(request, *args, **kwargs)
        # Wrap the response data in SaccessResponse.
        return SaccessResponse(response.data)


# Custom ListModelMixin to wrap the response in SaccessResponse when listing objects.
class SaccessListModelMixin(ListModelMixin):
    def list(self, request, *args, **kwargs):
        # Call the default list method and get the standard response.
        response = super().list(request, *args, **kwargs)
        # Wrap the response data in SaccessResponse.
        return SaccessResponse(response.data)


# Custom RetrieveModelMixin to wrap the response in SaccessResponse when retrieving an object.
class SaccessRetrieveModelMixin(RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        # Call the default retrieve method and get the standard response.
        response = super().retrieve(request, *args, **kwargs)
        # Wrap the response data in SaccessResponse.
        return SaccessResponse(response.data)


# Custom UpdateModelMixin to wrap the response in SaccessResponse after updating an object.
class SaccessUpdateModelMixin(UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        # Call the default update method and get the standard response.
        response = super().update(request, *args, **kwargs)
        # Wrap the response data in SaccessResponse.
        return SaccessResponse(response.data)


# Custom DestroyModelMixin to wrap the response in SaccessResponse after deleting an object.
class SaccessDestroyModelMixin(DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        # Call the default destroy method (no content returned by default).
        super().destroy(request, *args, **kwargs)
        # Return a custom message wrapped in SaccessResponse indicating the object was deleted.
        return SaccessResponse({'detail': 'Deleted'})
