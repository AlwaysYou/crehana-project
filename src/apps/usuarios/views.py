from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login as log_django
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

# own packages
from .forms import RegisterForm, LoginForm
from .tasks import email_welcome_signup
# Create your views here.

def crear_cuenta(request):
    header = "crear_cuenta"
    profile_form = RegisterForm(request.POST)
    if request.method == "POST":
        if profile_form.is_valid():
            email = request.POST.get('email', None)
            email_welcome_signup.delay(email)
            password = request.POST['password']
            profile_form.save(password)
            user = profile_form.auth(password)
            log_django(request, user)
            return redirect(reverse('web:home'))
        else:
            profile_form = RegisterForm()
    else:
        pass
    return render(request, 'usuarios/crear_cuenta.html', locals())


def login(request):
    header = "login"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.auth()
            if user:
                log_django(request, user)
                return redirect("web:home")
        else:
            error = True

    """ Si el usuario ya esta logeado """
    if request.user.is_authenticated:
        return redirect('web:home')

    return render(request, 'usuarios/login.html', locals())





@login_required(login_url=reverse_lazy('web:home'))
def user_logout(request):
    request.session.flush()
    return logout_then_login(request, reverse('usuarios:login'))


