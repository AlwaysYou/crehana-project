import culqipy
import json
from django.http import JsonResponse
import culqipy
from django.conf import settings

culqipy.public_key = settings.ENV.get('CULQI_PUBLIC_KEY')
culqipy.secret_key = settings.ENV.get('CULQI_SECRET_KEY')

def culqi_begin(profile, n_pedido, _token):
    token = json.loads(_token)

    data =  {'status': 'error', 'msj': ''}
    # Integrar log
    print(token, "<- Token")


