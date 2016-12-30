from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render_to_response
from dict.models import Words
from django.db import models

# Create your views here.
def serch_key(request):
    content = ""
    if "key" in request.GET:
        key = request.GET["key"] 
        
    return render_to_response("dict.html", locals())