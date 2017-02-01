from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http import HttpRequest,HttpResponse
from dict.models import Translate,Words
import re

# Create your views here.
def has_chinese_character(t_str):
	zhPattern = re.compile('[^\u4e00-\u9fa5]+')
	match = zhPattern.search(t_str)
	if match:
		return True
	else:
		return False

def serch_key(request):
    ct = request.GET.get("key", "")
    if ct != "":
        print(ct)
        t = Words.objects.get(id=1)
        print(t.word)
        try:
            #if has_chinese_character(ct):
            #    ct = Words.objects.get(word=ct.decode("GBK").encode("utf8"))
            #else:
            #    ct = Translate.objects.get(word=ct.decode("GBK").encode("utf8"))
            ct = Words.objects.get(id="1")            
        except:            
            print("qwert")
        finally:
            ct = "Not found"
        
        print(ct)
    return render_to_response("dict.html", {"content":ct})
