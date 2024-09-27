from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from src.saccess_response.response import SaccessResponse


class SaccessCreateModelMixin(CreateModelMixin):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return SaccessResponse(response.data)


class SaccessListModelMixin(ListModelMixin):
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return SaccessResponse(response.data)


class SaccessRetrieveModelMixin(RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return SaccessResponse(response.data)


class SaccessUpdateModelMixin(UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return SaccessResponse(response.data)


class SaccessDestroyModelMixin(DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return SaccessResponse({'detail': 'Deleted'})
