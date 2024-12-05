# Django Saccess Response

`django-saccess-response` is a Django REST Framework extension that provides a standardized success response format for API views. It simplifies handling both successful and error responses with customizable data structures.

## Installation

Install the package via pip:

```bash
pip install django-saccess-response
```

## Usage

In your Django views, use `SaccessResponse` to wrap the response data.

### Example: Standard Success Response

```python
from saccess_response.response import SaccessResponse
from rest_framework.views import APIView


class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'key': 'value'}
        return SaccessResponse(data)
```

### Result:

```json
{
    "success": true,
    "result": {
        "key": "value"
    }
}
```

### Example: Error Response

To handle errors, pass `saccess=False`:

```python
from saccess_response.response import SaccessResponse
from rest_framework.views import APIView


class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'key': 'value'}
        return SaccessResponse(data, saccess=False)
```

### Result:

```json
{
    "success": false,
    "result": {
        "detail": "error"
    }
}
```

## Error Handling

You can also customize Django REST Framework's error responses globally by modifying the `EXCEPTION_HANDLER` setting in your `settings.py`:

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'saccess_response.views.saccess_exception_handler'
}
```

This will format all exceptions using the `SaccessResponse` structure.

## Generic Views and ViewSets

This package also provides customized DRF generic views and viewsets for standardized response handling.

| Standard View                  | Saccess Equivalent                    |
|--------------------------------|---------------------------------------|
| `CreateAPIView`                | `SaccessCreateAPIView`                |
| `RetrieveAPIView`              | `SaccessRetrieveAPIView`              |
| `UpdateAPIView`                | `SaccessUpdateAPIView`                |
| `DestroyAPIView`               | `SaccessDestroyAPIView`               |
| `ListAPIView`                  | `SaccessListAPIView`                  |
| `RetrieveUpdateAPIView`        | `SaccessRetrieveUpdateAPIView`        |
| `RetrieveDestroyAPIView`       | `SaccessRetrieveDestroyAPIView`       |
| `RetrieveUpdateDestroyAPIView` | `SaccessRetrieveUpdateDestroyAPIView` |
| `ModelViewSet`                 | `SaccessModelViewSet`                 |
| `ReadOnlyModelViewSet`         | `SaccessReadOnlyModelViewSet`         |

These classes behave like their DRF counterparts but automatically format responses using `SaccessResponse`.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
