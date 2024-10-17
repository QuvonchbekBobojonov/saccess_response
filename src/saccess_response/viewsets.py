from rest_framework import viewsets
from .mixins import (
    SaccessCreateModelMixin,
    SaccessListModelMixin,
    SaccessRetrieveModelMixin,
    SaccessUpdateModelMixin,
    SaccessDestroyModelMixin
)


# This viewset provides read-only actions (list and retrieve) for the model.
class SaccessReadOnlyModelViewSet(SaccessListModelMixin, SaccessRetrieveModelMixin, viewsets.GenericViewSet):
    http_method_names = ['get', 'head', 'options']


# This viewset provides full CRUD operations for the model.
class SaccessModelViewSet(
    SaccessListModelMixin,
    SaccessCreateModelMixin,
    SaccessRetrieveModelMixin,
    SaccessUpdateModelMixin,
    SaccessDestroyModelMixin,
    viewsets.ModelViewSet  # Or use GenericViewSet depending on your mixins
):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']
