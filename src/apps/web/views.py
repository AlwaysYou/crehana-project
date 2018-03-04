from django.shortcuts import render
from apps.productos.models import Categoria, Curso
# Create your views here.

def home(request):
    cursos = Curso.objects.filter(mostrar_home=True).order_by('position')
    return render(request, 'web/home.html', locals())



