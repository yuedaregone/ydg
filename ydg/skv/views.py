# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response

from skv.models import Skv


def get_value(key):
    skvItem = None
    try:
        skvItem = Skv.objects.get(key=key)
    except:
        skvItem = None
    if skvItem is None:
        return None
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
            return HttpResponse("Key is none")

        val = get_value(key)
        if val is None:
            val = "Not Found!"
        return HttpResponse(val)
    else:
        key = request.POST.get("key", "")
        val = request.POST.get("value", "")
        set_value(key, val)
        return HttpResponse("OK")


def post_kv(request):
    if request.method == "POST":
        key = request.POST.get("key", "")
        val = request.POST.get("value", "")
        set_value(key, val)
        return list_kv(request)
    else:
        return HttpResponse("Error")


def list_kv(request):
    skvItems = Skv.objects.all()
    skvStr = "{"
    for item in skvItems:
        skvStr += "\"" + item.key + "\":\"" + item.value + "\","
    if len(skvItems) > 0:
        skvStr = skvStr[:len(skvStr) - 1] + "}"
    else:
        skvStr += "}"
    return HttpResponse(skvStr)


def add_kv(request):
    return render_to_response("skv.html", {})


def del_kv(request):
    delete = request.GET.get("del", "")
    if delete == "":
        return HttpResponse("del is none")
    try:
        skvItem = Skv.objects.get(key=delete)
        skvItem.delete()
        return HttpResponse("del is done")
    except:
        return HttpResponse("not found!")


def redirect_natapp(request):
    val = get_value("NatappUrl")
    if val is None:
        return list_kv
    return HttpResponsePermanentRedirect(val)


def redirect_ngrok(request):
    val = get_value("Ngrok")
    if val is None:
        return list_kv(request)
    return HttpResponsePermanentRedirect(val)
