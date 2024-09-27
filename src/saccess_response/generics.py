from rest_framework.generics import GenericAPIView
from src.saccess_response.mixins import SaccessCreateModelMixin, SaccessListModelMixin, SaccessRetrieveModelMixin, \
    SaccessUpdateModelMixin, SaccessDestroyModelMixin


class SaccessCreateAPIView(SaccessCreateModelMixin, GenericAPIView):
    pass


class SaccessListAPIView(SaccessListModelMixin, GenericAPIView):
    pass


class SaccessRetrieveAPIView(SaccessRetrieveModelMixin, GenericAPIView):
    pass


class SaccessUpdateAPIView(SaccessUpdateModelMixin, GenericAPIView):
    pass


class SaccessDestroyAPIView(SaccessDestroyModelMixin, GenericAPIView):
    pass


class SaccessListCreateAPIView(SaccessCreateModelMixin, SaccessListModelMixin, GenericAPIView):
    pass


class SaccessRetrieveUpdateAPIView(SaccessRetrieveModelMixin, SaccessUpdateModelMixin, GenericAPIView):
    pass


class SaccessRetrieveDestroyAPIView(SaccessRetrieveModelMixin, SaccessDestroyModelMixin, GenericAPIView):
    pass


class SaccessRetrieveUpdateDestroyAPIView(SaccessRetrieveModelMixin, SaccessUpdateModelMixin,
                                          SaccessDestroyModelMixin, GenericAPIView):
    pass
