# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from skv.models import Skv

def get_value(key):  
    skvItem = None
    try:
        skvItem = Skv.objects.get(key=key)
    except:
        skvItem = None
    if skvItem is None:
        return "Not Found!!"
    return skvItem.value

def set_value(key, val):
    skvItem = None
    try:
        skvItem = Skv.objects.get(key=key)
        skvItem.value = val
    except:
        skvItem = Skv(key=key, value=val)
    skvItem.save()

def select_key(request):
    if request.method == "GET":
        key = request.GET.get("key", "")
        if key == "":
            return render_to_response("skv.html", {})
        val = get_value(key)
        return HttpResponse(val)
    else:
        key = request.POST.get("key", "")
        val = request.POST.get("value", "")
        set_value(key, val)
        return HttpResponse("OK")



    