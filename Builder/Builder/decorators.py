from django.conf import settings
from django.http import HttpResponseForbidden
from functools import wraps

def internal_only(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        internal_key = request.headers.get('nocode_internal_key')
        if internal_key != settings.INTERNAL_API_KEY:
            return HttpResponseForbidden("This endpoint is internal-only.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view