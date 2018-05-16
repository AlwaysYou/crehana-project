from celery import task

from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings


@task
def email_welcome_signup(email):
    print("entro a la funcion sigmup")
    htmly = get_template('emails/email-create-user.html')
    email_destino = email
    d = Context(email_destino)
    html_content = htmly.render(d)
    asunto = u'Crehana: Bienvenido a la familia'
    mail = 'Crehana<{}>'.format(settings.DEFAULT_FROM_EMAIL)
    msg = EmailMessage(asunto, html_content, mail, [email_destino, ])
    msg.content_subtype = "html"
    try:
        msg.send()
        print("Envio correcto")
    except:
        pass


