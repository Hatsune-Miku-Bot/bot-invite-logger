from .discord import request_discord
from .discord.color import Color
from .discord.embeds import Embed
from .discord.meek_moe import meek_api
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.http import require_POST


# Create your views here.
def message_me(voterid: int=None,site: str=None):
    a = request_discord.discord_api_req(
        '/users/@me/channels',
        'post',
        data={
            'recipient_id': 571889108046184449
        }
    )
    json = a.json()
    embed=Embed(
        title='Thanks for voting me!',
        color=Color.random(),
        description=f'Thanks **{json["recipients"][0]["username"]}{json["recipients"][0]["discriminator"]}** for voting me! :heart: <:45:778253031523090443>',
        timestamp=datetime.utcnow()
    )
    b = request_discord.discord_api_req(
        f'/channels/{a.json()["id"]}/messages',
        'post',
        data={
            'embed':embed.to_dict()
        }
    )
    request_discord.discord_api_req(
        f'/channels/{a.json()["id"]}/messages',
        'post',
        data={
            'embed':meek_api()
        }
    )
    return HttpResponse('Done')