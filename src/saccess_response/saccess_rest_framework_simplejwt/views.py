from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from ..response import SaccessResponse


# Custom class for obtaining JWT access and refresh tokens, wrapping the response in SaccessResponse
class SaccessTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Call the original post method from TokenObtainPairView to handle token generation
        response = super().post(request, *args, **kwargs)
        # Return the token data in the custom SaccessResponse format
        return SaccessResponse(response.data)


# Custom class for refreshing JWT access tokens, wrapping the response in SaccessResponse
class SaccessTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Call the original post method from TokenRefreshView to handle token refresh
        response = super().post(request, *args, **kwargs)
        # Return the refreshed token data in the custom SaccessResponse format
        return SaccessResponse(response.data)


# Custom class for verifying JWT tokens, wrapping the response in SaccessResponse
class SaccessTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        # Call the original post method from TokenVerifyView to verify the token
        response = super().post(request, *args, **kwargs)
        # Return the verification result in the custom SaccessResponse format
        return SaccessResponse(response.data)
