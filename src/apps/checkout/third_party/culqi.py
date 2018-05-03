import culqipy
import json
from django.http import JsonResponse
import culqipy
from django.conf import settings


class Culqi(object):
    culqi_public_key = settings.ENV.get('CULQI_PUBLIC_KEY')
    culqi_secret_key = settings.ENV.get('CULQI_SECRET_KEY')
    culqipy.public_key = culqi_public_key
    culqipy.secret_key = culqi_secret_key

    def __init__(self, _token, profile, pedido=None):
        self.profile = profile
        self.token = json.loads(_token)
        self.pedido = pedido
        self.error = None

    #def create_card(self, token, pedido, profile):
