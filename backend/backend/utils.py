from django.db import connections
from django.core import serializers
from collections import OrderedDict
from django.http import HttpResponse,JsonResponse
import json

def execute(qs_list):
    print(qs_list)
    return HttpResponse(qs_list, content_type="text/json-comment-filtered")

def execute_and_serialize(qs):
    qs_list = serializers.serialize('json', qs)
    print(qs_list)
    return HttpResponse(qs_list, content_type="text/json-comment-filtered")    

def success_message():
    return_message = OrderedDict()
    return_message['code'] = 0
    return_message['msg'] = "ok"
    
    return json.dumps(return_message,ensure_ascii=False)

def errors_message(form):
    return_message = OrderedDict()
    return_message['code'] = -1
    return_message['msg'] = form.errors
    
    return json.dumps(return_message,ensure_ascii=False)

