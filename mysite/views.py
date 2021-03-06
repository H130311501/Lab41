# -*- coding: utf-8 -*-
"""
Created on Mon Nov 02 20:55:58 2015

@author: Administrator
"""

from django.http import Http404,HttpResponse
from django.template import Template,Context
import datetime
def hello(request):
     return HttpResponse("Hello Word!")
     
def current_datetime(request):
    now=datetime.datetime.now()
    t=Template("<html><body>It is now{{ current_date}}.</body></html>") 
    html=t.render(Context({'current_date':now}))
    return HttpResponse(html)
    
def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>In %s hour(s),it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)
    
        