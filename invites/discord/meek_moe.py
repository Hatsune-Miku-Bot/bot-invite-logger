from os.path import join
from pathlib import Path
from random import choice

import requests

from .color import Color
from .embeds import Embed


def meek_api(name='miku'):
    l = choice(['https://api.meek.moe/', 'https://mikuapi.predeactor.net/random',False]) if name.lower() == 'miku' else 'https://api.meek.moe/'
    e=Embed(title='Arigato! <:45:778253031523090443>',color=Color.random())
    try:
        if name=='miku' and l:
            data = requests.get(url = l + name if l=='https://api.meek.moe/' else 'https://mikuapi.predeactor.net/random').json()['url']
        else:
            data = requests.get(url = l + name).json()['url']
        e.set_image(url=data)
    except:
        imageslistdir = Path(__file__).resolve(
                strict=True).parent / join('images_list.txt')
        filepointer = open(imageslistdir)
        imageslist = filepointer.readlines()
        if name == 'miku':
            e.set_image(url=choice(imageslist))
        else:
            e=Embed(title='Sorry but currently there is some problem!',color=Color.red())
            e.set_image(url=choice(imageslist))
    return e.to_dict()
