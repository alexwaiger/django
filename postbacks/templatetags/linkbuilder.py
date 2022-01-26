# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def build(value, gambler_id):
    link = value
    if link.endswith('&'):
        link = link
    elif 'bit.ly' in link:
        link = link
    elif link.endswith('anid='):
        link = link[:-5]
    elif link.endswith('clickid={clickid}'):
        link = link[:-17]
    elif 'refpasrasw' in link:
        link = link[:-1] + '&'
    elif link.endswith('#popup-reg') or 'media' in link:
        link = link + '&'
    elif link.endswith('r=registration/'):
        link = link[:-1] + '&'
    elif '&' not in link and '?' not in link:
        if link.endswith('/'):
            link = link + '?'
        else:
            link = link + '/?'
    elif '?' in link and '&' not in link:
        link = link + '&'       
    else:
        link = link
    
    if 'bit.ly' in link:
        fulllink = link
    else:
        fulllink = link + 'anid=' + gambler_id + '&payload=' + gambler_id + '&clickid=' + gambler_id + '&s2s.req_id=' + gambler_id + '&gklid=' + gambler_id + '&click_id=' + gambler_id + '&subid=' + gambler_id + '&cid=' + gambler_id + '&var=' + gambler_id + '&sub_id1=' + gambler_id + '&s2=' + gambler_id + '&visit_id=' + gambler_id 
    return fulllink