ITEMS = {
    'insta': {
        'logo': '../static/logos/ic_instagram.png',
        'class': 'soc-href-card-instagram'
    },
    'vk': {
        'logo': '../static/logos/ic_vk.png',
        'class': 'soc-href-card-vk'
    },
    'telegram': {
        'logo': '../static/logos/ic_tg.png',
        'class': 'soc-href-card-tg'
    },
    't.me': {
        'logo': '../static/logos/ic_tg.png',
        'class': 'soc-href-card-tg'
    },
    'viber': {
        'logo': '../static/logos/ic_viber.png',
        'class': 'soc-href-card-viber'
    },
    'whatsapp': {
        'logo': '../static/logos/ic_whatsapp.png',
        'class': 'soc-href-card-whatsapp'
    },
    'facebook': {
        'logo': '../static/logos/ic_facebook.png',
        'class': 'soc-href-card-facebook'
    },
    'youtube': {
        'logo': '../static/logos/ic_youtube.png',
        'class': 'soc-href-card-youtube'
    },
    'skype': {
        'logo': '../static/logos/ic_skype.png',
        'class': 'soc-href-card-skype'
    },
    'linkedin': {
        'logo': '../static/logos/ic_linkedin.png',
        'class': 'soc-href-card-linkedin'
    },
    'wildberries': {
        'logo': '../static/logos/ic_wildberries.png',
        'class': 'soc-href-card-wildberries'
    },
    'tiktok': {
        'logo': '../static/logos/ic_tik-tok.png',
        'class': 'soc-href-card-tik-tok'
    },
    'ok': {
        'logo': '../static/logos/ic_ok.png',
        'class': 'soc-href-card-ok'
    },
    '2gis': {
        'logo': '../static/logos/ic_2gis.png',
        'class': 'soc-href-card-2gis'
    },
    'all': {
        'logo': '../static/logos/ic_all.png',
        'class': 'soc-href-card-all'
    },
}

DEFAULT = {
    "ok": {
        'link': "https://ok.ru",
        'logo': '../static/logos/ic_ok.png',
        'class': 'soc-href-card-ok'
    },
    "youtube": {
        'link': "https://youtu.be",
        'logo': '../static/logos/ic_ok.png',
        'class': 'soc-href-card-ok'
    },
}


def get_item(url: str, content_type: str):
    for key, value in DEFAULT.items():
        if url.startswith(value['link']):
            return ITEMS[key][content_type]

    for key in ITEMS:
        if key in url:
            return ITEMS[key][content_type]
    return ITEMS['all'][content_type]
