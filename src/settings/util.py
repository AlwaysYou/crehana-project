# -*- coding: utf-8 -*-
import json
from os.path import join


def get_env(base_dir):
    """ Obtenemos las 'variables de entorno' desde un archivo json."""
    print(base_dir)
    with open(join(base_dir, 'settings/settings.json'), encoding='utf-8-sig') as f:
        env = json.load(f)
        return env
    return {}
