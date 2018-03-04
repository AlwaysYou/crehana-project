from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'usuarios/login.html', locals())

def crear_cuenta(request):
    return render(request, 'usuarios/crear_cuenta.html', locals())


