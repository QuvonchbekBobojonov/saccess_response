# Django rest framework app for customizing response data

## Installation

```bash
pip install django-saccess-response
```

## Usage

```python
from saccess_response.response import SaccessResponse
from rest_framework.views import APIView


class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'key': 'value'}
        return SaccessResponse(data)
```
result:
```json
{
    "status": true,
    "result": {
        "key": "value"
    }
}
```


## Error Handling

```python
from saccess_response.response import SaccessResponse
from rest_framework.views import APIView

class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'key': 'value'}
        return SaccessResponse(data, saccess=False)
```

result:
```json
{
    "status": false,
    "result": {
        "detail": "error"
    }
}
```

## Custom Django Rest Framework error handling

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'saccess_response.views.saccess_exception_handler'
}
```

## Ganeric View and ViewSet class name

- **CreateAPIView**: `SaccessCreateAPIView`
- **RetrieveAPIView**: `SaccessRetrieveAPIView`
- **UpdateAPIView**: `SaccessUpdateAPIView`
- **DestroyAPIView**: `SaccessDestroyAPIView`
- **ListAPIView**: `SaccessListAPIView`
- **RetrieveUpdateAPIView**: `SaccessRetrieveUpdateAPIView`
- **RetrieveDestroyAPIView**: `SaccessRetrieveDestroyAPIView`
- **RetrieveUpdateDestroyAPIView**: `SaccessRetrieveUpdateDestroyAPIView`
- **ModelViewSet**: `SaccessModelViewSet`
- **ReadOnlyModelViewSet**: `SaccessReadOnlyModelViewSet`
