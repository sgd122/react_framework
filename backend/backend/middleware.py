from django.db.models import Model, QuerySet
from django.http import HttpResponse, JsonResponse
from .encoders import JSONEncoder


def json_response_middleware(get_response):
    def middleware(request, *args):
        response = get_response(request)
        if isinstance(response, str):
            if response and response[0] in ('"', '[', '{'):
                response = HttpResponse(response, content_type='application/json')
            else:
                response = HttpResponse(response)
        elif isinstance(response, (set, dict, list, tuple, QuerySet, Model)):
            response = JsonResponse(response, encoder=JSONEncoder,
                                    json_dumps_params={'ensure_ascii': False}, safe=False)

        if not request.path.startswith('/admin'):
            response['Access-Control-Allow-Origin'] = request.META.get('HTTP_ORIGIN', '*')
            response['Access-Control-Allow-Headers'] = 'ACCEPT,ACCEPT-ENCODING,CONTENT-TYPE,ORIGIN,' \
                                                       'USER-AGENT,X-REQUESTED-WITH'
            response['Access-Control-Allow-Methods'] = "*"
            response['Access-Control-Allow-Credentials'] = 'true'
            
        return response
    return middleware


