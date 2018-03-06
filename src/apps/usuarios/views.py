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
    header = "login"
    if request.method == "POST":
        error = False
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.auth()
            """ Si existe el usuario """
            if user:
                log_django(request, user)
                return redirect("web:home")
            else:
                error = True
        else:
            error = True

    """ Si el usuario ya ha sido logeado """
    if request.user.is_authenticated:
        return redirect('web:home')

    return render(request, 'usuarios/login.html', locals())


def crear_cuenta(request):
    header = "crear_cuenta"
    error = False
    profile_form = RegisterForm(request.POST)
    """ Si es un metodo POST """
    if request.method == "POST":
        if profile_form.is_valid():
            password = request.POST['password']
            profile_form.save(password)
            profile_form.enviaEmail()
            user = profile_form.auth(password)
            log_django(request, user)
            return redirect(reverse('web:home'))
        else:
            error = True
            profile_form = RegisterForm()
    else:
        pass
    return render(request, 'usuarios/crear_cuenta.html', locals())


@login_required(login_url=reverse_lazy('web:home'))
def user_logout(request):
    request.session.flush()
    return logout_then_login(request, reverse('usuarios:login'))


