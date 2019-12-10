from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from backend.decorators import api_view
from backend.utils import errors_message,success_message,execute,execute_and_serialize
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django import views
import json
from .serializers import BlogSerializer,MenuSerializer
from rest_framework import generics
from .form import Blog_Form,Menu_Form
from .models import Blog,Menu
from collections import OrderedDict

# Create your views here.
class MasterBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class DetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class SaveBlog(views.View):
    @method_decorator(csrf_exempt)
    # @api_view
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)        
    def get(self, request):
        return_message = OrderedDict()
        return_message['code'] = -1
        return_message['msg'] = "error"
        
        return json.dumps(return_message,ensure_ascii=False)
    def post(self, request):
        data = json.loads(request.body)
        form = Blog_Form(data)
        if data.get('id') != None:
            post = get_object_or_404(Blog,pk=data['id'])
            form = Blog_Form(data, instance=post)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return success_message()      
        else:
            print(errors_message(form))
            return errors_message(form)
    def delete(self, request):
        data = json.loads(request.body)
        form = Blog_Form(data)
        if data.get('id') != None:
            post = get_object_or_404(Blog,pk=data['id'])
            form = Blog_Form(data, instance=post)
        if form.is_valid():            
            blog = form.delete(commit=False)
            blog.delete()
            return success_message()      
        else:
            print(errors_message(form))
            return errors_message(form)     



##################################################
# MENU
##################################################

class MasterMenu(generics.ListCreateAPIView):
    queryset = Menu.objects.all().order_by('code','sort')
    serializer_class = MenuSerializer

class DetailMenu(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all().order_by('code','sort')
    serializer_class = MenuSerializer

class SaveMenu(views.View):
    @method_decorator(csrf_exempt)
    # @api_view
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)        
    def get(self, request):
        return_message = OrderedDict()
        return_message['code'] = -1
        return_message['msg'] = "error"
        
        return json.dumps(return_message,ensure_ascii=False)
    def post(self, request):
        data = json.loads(request.body)
        form = Menu_Form(data)
        if data.get('id') != None:
            post = get_object_or_404(Menu,pk=data['id'])
            form = Menu_Form(data, instance=post)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return success_message()      
        else:
            print(errors_message(form))
            return errors_message(form)
    def delete(self, request):
        data = json.loads(request.body)
        form = Menu_Form(data)
        if data.get('id') != None:
            post = get_object_or_404(Menu,pk=data['id'])
            form = Menu_Form(data, instance=post)
        if form.is_valid():            
            menu = form.delete(commit=False)
            menu.delete()
            return success_message()      
        else:
            print(errors_message(form))
            return errors_message(form)

@api_view
def SaveMenu2(request):   
    form = Menu_Form(request.JSON)
    if request.method == 'POST':
        if request.JSON.get('id') != None:
            post = get_object_or_404(Menu,pk=request.JSON['id'])
            form = Menu_Form(request.JSON, instance=post)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return success_message()      
        else:
            print(errors_message(form))
            return errors_message(form)
    elif request.method == 'DELETE':
        if form.is_valid():            
            menu = form.delete(commit=False)
            menu.delete()
            return success_message()      
        else:            
            print(errors_message(form))
            return errors_message(form)        
    else:
        return errors_message(form)
