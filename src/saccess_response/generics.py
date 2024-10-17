from rest_framework.generics import GenericAPIView
from .mixins import SaccessCreateModelMixin, SaccessListModelMixin, SaccessRetrieveModelMixin, \
    SaccessUpdateModelMixin, SaccessDestroyModelMixin


# Custom API view for creating objects. Inherits from SaccessCreateModelMixin.
class SaccessCreateAPIView(SaccessCreateModelMixin, GenericAPIView):

    # Handle POST requests to create an object.
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Custom API view for listing objects. Inherits from SaccessListModelMixin.
class SaccessListAPIView(SaccessListModelMixin, GenericAPIView):

    # Handle GET requests to list objects.
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Custom API view for retrieving a single object. Inherits from SaccessRetrieveModelMixin.
class SaccessRetrieveAPIView(SaccessRetrieveModelMixin, GenericAPIView):

    # Handle GET requests to retrieve a specific object by its ID.
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Custom API view for updating an object. Inherits from SaccessUpdateModelMixin.
class SaccessUpdateAPIView(SaccessUpdateModelMixin, GenericAPIView):

    # Handle PUT requests to update an entire object.
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Handle PATCH requests to partially update an object.
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# Custom API view for deleting an object. Inherits from SaccessDestroyModelMixin.
class SaccessDestroyAPIView(SaccessDestroyModelMixin, GenericAPIView):

    # Handle DELETE requests to remove an object.
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Combined List and Create API view. Handles both GET (list) and POST (create).
class SaccessListCreateAPIView(SaccessCreateModelMixin, SaccessListModelMixin, GenericAPIView):

    # Handle GET requests to list objects.
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Handle POST requests to create a new object.
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Combined Retrieve and Update API view. Handles both GET (retrieve) and PUT/PATCH (update).
class SaccessRetrieveUpdateAPIView(SaccessRetrieveModelMixin, SaccessUpdateModelMixin, GenericAPIView):

    # Handle GET requests to retrieve an object.
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Handle PUT requests to update an object.
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Handle PATCH requests to partially update an object.
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# Combined Retrieve and Destroy API view. Handles both GET (retrieve) and DELETE (destroy).
class SaccessRetrieveDestroyAPIView(SaccessRetrieveModelMixin, SaccessDestroyModelMixin, GenericAPIView):

    # Handle GET requests to retrieve an object.
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Handle DELETE requests to remove an object.
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Combined Retrieve, Update, and Destroy API view. Handles GET (retrieve), PUT/PATCH (update), and DELETE (destroy).
class SaccessRetrieveUpdateDestroyAPIView(SaccessRetrieveModelMixin, SaccessUpdateModelMixin,
                                          SaccessDestroyModelMixin, GenericAPIView):

    # Handle GET requests to retrieve an object.
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Handle PUT requests to update an object.
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Handle PATCH requests to partially update an object.
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # Handle DELETE requests to remove an object.
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
