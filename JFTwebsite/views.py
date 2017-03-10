from django.http import HttpResponse, Http404
from django.template.loader import get_template 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .settings import MEDIA_ROOT
import datetime
import os
from os import listdir
from os.path import isfile, join
from jftcv.models import Router

 
def brushuppages(request,htmlfile):
    brushuppath="BrushUp/"
    onlyfiles = [f for f in listdir(brushuppath) if isfile(join(brushuppath, f))]
    if str(htmlfile)+".html" not in onlyfiles:
        raise Http404() 
    else:
        """
        text=""
        This can be done without the use of templates as follows:
        mfile=open(brushuppath+str(htmlfile)+".html","r") 
        for line in mfile:
            text+=line
        mfile.close()
        """
        t = get_template(str(htmlfile)+".html") 
        text=t.render()
        return HttpResponse(text) 

def cvcredits(request):
    cvpath="CVOnline/"
    onlyfiles = [f for f in listdir(cvpath) if isfile(join(cvpath, f))]
    print(onlyfiles)
    if "credits.html" not in onlyfiles:
        raise Http404() 
    else:
        t = get_template("credits.html") 
        text=t.render()
        return HttpResponse(text) 	

def download_CV(request,user):
  try:
    print(user,MEDIA_ROOT,Router.objects.filter(owner=user)[0].specifications)
    cvfile=Router.objects.filter(owner=user)[0].specifications
    file_path = os.path.join(str(MEDIA_ROOT), str(cvfile))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404
  except IndexError:
    raise Http404
