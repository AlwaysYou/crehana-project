from django.shortcuts import render

# Create your views here.

def mi_carrito(request):
    return render(request, 'pedidos/mi_carrito.html', locals())


