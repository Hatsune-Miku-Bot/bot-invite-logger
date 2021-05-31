from datetime import datetime

from django.conf import settings

from .discord import request_discord
from .discord.color import Color
from .discord.embeds import Embed
from .discord.meek_moe import meek_api

list_dict = {
    'Top.GG': 'https://top.gg/images/dblnew.png',
    'Discordlist Space': 'https://discordlist.space/img/apple-touch-icon.png',
    'Bots For Discord': 'https://botsfordiscord.com/img/favicons/apple-touch-icon-57x57.png',
    'Discord Bot List': 'https://discordbotlist.com/ms-icon-144x144.png',
    'Discord Boats': 'https://discord.boats/apple-icon-57x57.png',
    'Fates List': 'https://fateslist.xyz/static/botlisticon.webp',
    'Blade Bot List': 'https://bladebotlist.xyz/img/logo.png',
    'Void Bots': 'https://voidbots.net/assets/img/logo.png',
    'LOCAL': 'https://i.imgur.com/vlBPK30.png'
}
site_dict = {
    'Top.GG': f'https://top.gg/bot/{settings.DISCORDBOTID}',
    'Discordlist Space': f'https://discordlist.space/bot/{settings.DISCORDBOTID}',
    'Bots For Discord': f'https://botsfordiscord.com/bot/{settings.DISCORDBOTID}',
    'Discord Bot List': f'https://discordbotlist.com/bots/{settings.DISCORDBOTID}',
    'Discord Boats': f'https://discord.boats/bot/{settings.DISCORDBOTID}',
    'Fates List': f'https://fateslist.xyz/bot/{settings.DISCORDBOTID}',
    'Blade Bot List': f'https://bladebotlist.xyz/bot/{settings.DISCORDBOTID}',
    'Void Bots': f'https://voidbots.net/bot/{settings.DISCORDBOTID}/',
    'LOCAL': 'https://i.imgur.com/vlBPK30.png'
}

def message_me(voterid: int,site: str):
    try:
        a = request_discord.discord_api_req(
            '/users/@me/channels',
            'post',
            data={
                'recipient_id': voterid
            }
        )
        json = a.json()
        user_pfp = f'https://cdn.discordapp.com/avatars/{voterid}/{json["recipients"][0]["avatar"]}.webp?size=1024'
        embed=Embed(
            title=f'Thanks for voting me! on {site}',
            color=Color.random(),
            description=f'Thanks **<@!{json["recipients"][0]["id"]}>** ({json["recipients"][0]["username"]}#{json["recipients"][0]["discriminator"]}) for voting me! :heart: <:45:778253031523090443>',
            timestamp=datetime.utcnow()
        )
        embed.set_author(
            name=site,
            url=site_dict[site],
            icon_url = list_dict[site]
        )
        embed.set_thumbnail(url=user_pfp)
        
        request_discord.discord_api_req(
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
        request_discord.discord_api_req(
            '/channels/848506780912058389/messages',
            'post',
            data={
                'embed':embed.to_dict()
            }
        )
    except Exception as e:
        a = request_discord.discord_api_req(
            '/users/@me/channels',
            'post',
            data={
                'recipient_id': 571889108046184449
            }
        )
        json = a.json()
        request_discord.discord_api_req(
            '/channels/848506780912058389/messages',
            'post',
            data={
                'embed':embed.to_dict()
            }
        )
