from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from src.saccess_response.response import SaccessResponse


class SaccessTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return SaccessResponse(response.data)


class SaccessTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return SaccessResponse(response.data)


class SaccessTokenVerifyView(TokenVerifyView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return SaccessResponse(response.data)
