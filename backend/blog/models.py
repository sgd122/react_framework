from django.db import models
from backend.utils import execute,execute_and_serialize,errors_message
from django.core.validators import ValidationError # validation
import re

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.
class Blog(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=50, null=True)
    surname = models.CharField('surname', max_length=50, null=True)
    birthYear = models.IntegerField('birthYear', null=True)
    birthCity = models.CharField('birthCity', max_length=50, null=True)
    lnglat = models.CharField(max_length=50, blank=True, null=True,
        validators = [lnglat_validator], # 함수를 넘겨서 유효성 검사 실행
        help_text='경도, 위도 포맷으로 입력')

class Menu(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=50, null=True)
    code = models.CharField('code', max_length=50, null=True)
    menu_parent = models.CharField('menu_parent', max_length=50, null=True)
    link = models.CharField('link', max_length=200, null=True)
    level = models.IntegerField('level', null=True)
    sort = models.IntegerField('sort', null=True)
