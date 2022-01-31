# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

import random

register = template.Library()

@register.filter(name='build')
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


@register.filter(name='rating', is_safe=True)
def dynamic_rating(position):
    rating = 50 - position
    rating = str(rating)
    rating = rating[0] + '.' + rating[1]
    return rating

@register.filter(name='stars', is_safe=True)
def dynamic_stars(position):
    rating = 50 - position
    if rating < 40 and rating > 30:
        rating = 35
    elif rating < 30 and rating > 20:
        rating = 25
    elif rating < 20 and rating > 10:
        rating = 15
    else:
        rating = rating
    return rating

@register.filter(name='votes', is_safe=True)
def dynamic_votes(position):
    votes = (50 - position)
    res_votes = votes * random.randint(votes, votes*2)
    return res_votes