from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings


class RegisterForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        profiles = UserProfile.objects.filter(email=email)
        if profiles:
            raise forms.ValidationError('El email ya ha sido registrado')
        return email

    def save(self, password):
        profile = super(RegisterForm, self).save(commit=False)
        email = self.cleaned_data['email']
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        profile.user = user
        profile.save()
        return profile

    def auth(self, password):
        email = self.cleaned_data['email']
        return authenticate(username=email, password=password)

    def enviaEmail(self):
        htmly = get_template('emails/email-create-user.html')
        c_d = self.cleaned_data
        email_destino = c_d['email']
        d = Context(c_d)
        html_content = htmly.render(d)
        asunto = u'Crehana: Bienvenido a la familia'
        mail = 'Crehana<{}>'.format(settings.DEFAULT_FROM_EMAIL)
        msg = EmailMessage(asunto, html_content, mail, [email_destino, ])
        msg.content_subtype = "html"
        try:
            msg.send()
        except:
            pass

    class Meta:
        model = UserProfile
        fields = ('email',)


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    email.widget.attrs.update({'autofocus': 'true', 'tabindex': '1'})
    password = forms.CharField(label='Contraseña', min_length=6,
                               max_length=32, widget=forms.PasswordInput)
    password.widget.attrs.update({'tabindex': '2'})

    def clean_email(self):
        email = self.cleaned_data['email']
        email = email.lower()
        try:
            UserProfile.objects.get(user__username=email)
        except UserProfile.DoesNotExist:
            mensaje = u'El email no ha sido registrado'
            raise forms.ValidationError(mensaje)
        return email

    def auth(self):
        email = self.cleaned_data['email']
        email = email.lower()
        password = self.cleaned_data['password']

        profile = UserProfile.objects.get(user__username=email)
        username = profile.user.username

        return authenticate(username=username, password=password)
