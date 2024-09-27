from rest_framework.viewsets import ViewSetMixin
from src.saccess_response.mixins import SaccessCreateModelMixin, SaccessListModelMixin, SaccessRetrieveModelMixin, \
    SaccessUpdateModelMixin, SaccessDestroyModelMixin


class SaccessReadOnlyModelViewSet(SaccessListModelMixin, SaccessRetrieveModelMixin, ViewSetMixin):
    pass


class SaccessModelViewSet(SaccessListModelMixin, SaccessCreateModelMixin, SaccessRetrieveModelMixin,
                          SaccessUpdateModelMixin, SaccessDestroyModelMixin, ViewSetMixin):
    pass
