
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime


def fuckme(request):
    """api example."""
    assert isinstance(request, HttpRequest)
    return HttpResponse("MDZZ")