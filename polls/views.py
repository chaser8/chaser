import json

from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import AgreeCatalog
from django.core import serializers

def index(request):
    objects_all = AgreeCatalog.objects.all()
    serializers_serialize = serializers.serialize("json", objects_all, ensure_ascii=False)
    for o in objects_all:
        print(o.catalogName)
    ret = serialize("json", objects_all)
    return HttpResponse(serializers_serialize, content_type='application/json; charset=utf-8')
