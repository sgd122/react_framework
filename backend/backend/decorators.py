from functools import wraps
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def api_view(view_fn):
    @csrf_exempt
    @wraps(view_fn)
    def wrap(request, *args, **kwargs):
        try:
            request.JSON = json.loads(request.body)
        except ValueError as e:
            print(e)
            request.JSON = {}

        return view_fn(request, *args, **kwargs)
    return wrap
