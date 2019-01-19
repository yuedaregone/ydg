from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http import HttpRequest,HttpResponse
import os

def wintoy_list():
    curdir = os.path.abspath('.')
    curdir = curdir + "/res/toys/"

    ret = ""
    for f in os.listdir(curdir):
        ret += f + ","
    resp = HttpResponse(ret)
    return resp

def read_file(name):
    content = ""
    try:
        f = open(name, 'r')
        content = f.read()
    finally:
        if f:
            f.close()
    return content

def wintoy_file(name):
    curdir = os.path.abspath('.')
    curdir = curdir + "/res/toys/"
    name = curdir + name
    return HttpResponse(read_file(name))

def wintoy_response(request):   
    method = request.GET.get("method")
    if method == "list":
        return wintoy_list()
    if method == "file":
        name = request.GET.get("name")
        return wintoy_file(name)
    return HttpResponse("Hello,World!")


    

    
