from django.shortcuts import render
# import logging
from django.http import HttpResponse
import datetime


# logger = logging.getLogger(__name__)

def index(request):
    # logger.error('Something went wrong!')
    print ("Hello world")
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    
