"""ydg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dict.views import serch_key
from main.views import *
from wintoy.views import *
from skv.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dict/', serch_key),
    url(r'wintoy', wintoy_response),
    url(r'^skv/list', list_kv),
    url(r'^skv/add', add_kv),
    url(r'^skv/post_kv', post_kv),
    url(r'^skv/del', del_kv),
    url(r'^skv$', select_key),
    url(r'^ngrok$', redirect_ngrok),
    url(r'^natapp$', redirect_natapp),
    url(r'', main_view),    
]
