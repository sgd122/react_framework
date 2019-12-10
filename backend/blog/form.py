from django import forms
from django.shortcuts import get_object_or_404, render
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from backend.utils import execute,execute_and_serialize
from .models import Blog,Menu
import json
class Blog_Form(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields='__all__'        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id"] = forms.CharField(
            required=False,
        )
        for field_name, field in self.fields.items():            
            field.required = False
    
    def delete(self, commit=True):
        self.instance = Blog(**self.cleaned_data)
        if commit:
            self.instance.delete()
        return self.instance

class Menu_Form(forms.ModelForm):
    
    class Meta:
        model = Menu
        fields='__all__'        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id"] = forms.CharField(
            required=False,
        )
        for field_name, field in self.fields.items():
            field.required = False
    
    def delete(self, commit=True):
        self.instance = Menu(**self.cleaned_data)
        if commit:
            self.instance.delete()
        return self.instance
