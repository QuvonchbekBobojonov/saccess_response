from rest_framework.pagination import PageNumberPagination
from src.saccess_response.response import SaccessResponse


class SaccessPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return SaccessResponse({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'next_link': self.get_next_link(),
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'previous_link': self.get_previous_link(),
            'result': data
        })

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 100
                },
                'total_pages': {
                    'type': 'integer',
                    'example': 10
                },
                'current_page': {
                    'type': 'integer',
                    'example': 1
                },
                'next': {
                    'type': 'integer',
                    'example': 2,
                    'nullable': True
                },
                'next_link': {
                    'type': 'string',
                    'example': 'https://example.com/api/v1/users/?{page_query_param}=2'.format(page_query_param=self.page_query_param),
                    'nullable': True,
                    'format': 'uri'
                },
                'previous': {
                    'type': 'integer',
                    'example': 1,
                    'nullable': True
                },
                'previous_link': {
                    'type': 'string',
                    'example': 'https://example.com/api/v1/users/?{page_query_param}=1'.format(page_query_param=self.page_query_param),
                    'nullable': True,
                    'format': 'uri'
                },
                'result': schema
            }
        }
