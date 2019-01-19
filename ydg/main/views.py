from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http import HttpRequest,HttpResponse
import re

def main_view(request):    
    return render_to_response("index.html", {})

    
