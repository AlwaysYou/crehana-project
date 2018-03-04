from django.shortcuts import render
from django.template import RequestContext as ctx

# Create your views here.

def home(request):
    return render(request, 'web/home.html', locals())


