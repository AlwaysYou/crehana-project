import culqipy
import json
from django.http import JsonResponse


def culqi_begin(profile, n_pedido, _token):
    token = json.loads(_token)

    data =  {'status': 'error', 'msj': ''}
	# Integrar log

