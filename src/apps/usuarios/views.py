from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login as log_django
from django.core.urlresolvers import reverse_lazy

#logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

# own packages
from .forms import RegisterForm, LoginForm
# Create your views here.


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.auth()
            if user:
                log_django(request, user)
                return redirect("web:home")
                print("LOGIN DENTOR DEL IF USER")
            else:
                print("NO EXISTE USER")
        else:
            print(form.errors, "<- errors")
            error = form.errors
            print("FORM INVALIDO")

    if request.user.is_authenticated:
        print(request.user)
        return redirect('web:home')

    return render(request, 'usuarios/login.html', locals())

def crear_cuenta(request):
    print("Crear cuenta!")
    print(request.method, "<- metodo")
    print(request.POST, "<- POST DATA")
    profile_form = RegisterForm(request.POST)
    if request.method == "POST":
        print("soy post")
        if profile_form.is_valid():
            print("soy valido")
            password = request.POST['password']
            profile_form.save(password)

            user = profile_form.auth(password)
            log_django(request, user)
            return redirect(reverse('web:home'))
        else:
            print(profile_form.errors, "<- errores del form")
            profile_form = RegisterForm()
            return HttpResponseRedirect("/?error/")
    else:
        print("no soy POST")
    return render(request, 'usuarios/crear_cuenta.html', locals())


@login_required(login_url=reverse_lazy('web:home'))
def user_logout(request):
    request.session.flush()
    return logout_then_login(request, reverse('usuarios:login'))


