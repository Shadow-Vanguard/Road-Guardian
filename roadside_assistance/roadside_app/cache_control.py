from django.utils.cache import patch_cache_control
from django.utils.deprecation import MiddlewareMixin

# class CacheControlMiddleware(MiddlewareMixin):
#     def process_response(self, request, response):
#         # This will apply the cache control headers to the response
#         patch_cache_control(response, no_cache=True, no_store=True, must_revalidate=True)
#         return response

from django.utils.cache import patch_cache_control

class CacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        patch_cache_control(response, no_cache=True, no_store=True, must_revalidate=True)
        return response
