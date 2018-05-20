
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

from app.models import TestTable

def fuckme(request):
    """api example."""
    assert isinstance(request, HttpRequest)
    test = TestTable(name = 'caonima')
    test.save()
    for li in TestTable.objects.all():
        print str(li.name)
 
    return HttpResponse("mdzz")