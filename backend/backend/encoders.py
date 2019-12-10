import types
from base64 import b64encode
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from django.db.models import Model
from django.http import JsonResponse


class JSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, bytes):
            return b64encode(o).decode('ascii')
        elif hasattr(o, 'as_dict'):
            return o.as_dict()
        elif hasattr(o, 'as_list'):
            return o.as_list()
        elif isinstance(o, (set, types.GeneratorType, QuerySet)):
            return tuple(o)
        elif isinstance(o, Model):
            return {
                'id': o.id,
                'message': 'not implemented as_dict()',
            }
        return super().default(o)

