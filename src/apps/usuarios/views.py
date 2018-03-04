from django.shortcuts import render
from django.template import RequestContext as ctx

# Create your views here.

def login(request):
    return render(request, 'usuarios/login.html', locals())


