# -*- coding: utf-8 -*-

try:
    from urllib.request import urlopen # Python 3+
except ImportError:
    from urllib2 import urlopen # Python < 3
    
from django.views.generic import ListView
from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.conf import settings

import random
import os
import numpy as np

import requests
import json

import re

from itertools import chain

from django.utils import translation

from .models import Casino, Software, Countries
from postbacks.models import Postback, Partner

from django.views.decorators.cache import never_cache

from django.http import Http404, HttpResponseNotFound
    
def get_client_ip(request):
    if request.META.get('HTTP_CF_CONNECTING_IP'):
        ip = request.META.get('HTTP_CF_CONNECTING_IP')
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@never_cache
def home(request):
    gambler_id = {}
    if request.GET:
        if 'gclid' in request.GET:
            gambler_id['gclid'] = request.GET['gclid']
        if 'utm_term' in request.GET:
            gambler_id['utm_term'] = request.GET['utm_term']
        if 'utm_creative' in request.GET:
            gambler_id['utm_creative'] = request.GET['utm_creative']
        if 'utm_compaign' in request.GET:
            gambler_id['utm_compaign'] = request.GET['utm_compaign']
        if 'utm_position' in request.GET:
            gambler_id['utm_position'] = request.GET['utm_position']
        if 'utm_network' in request.GET:
            gambler_id['utm_network'] = request.GET['utm_network']
        if 'utm_target' in request.GET:
            gambler_id['utm_target'] = request.GET['utm_target']
        if 'utm_placement' in request.GET:
            gambler_id['utm_placement'] = request.GET['utm_placement']
        if 'utm_match' in request.GET:
            gambler_id['utm_match'] = request.GET['utm_match']
    else:
        gambler_id=False

    params = ''
    if gambler_id:
        for id in gambler_id:
            if params == '':
                params = '?'
            else:
                params += '&'
            params += id + '=' + gambler_id[id]
        
    headers = {
        "Content-type": "application/json",
        "Accept": "text/plain",
        "Content-Encoding": "utf-8"
    }
    country_lang = settings.SITE_LANGUAGE
    country_slug = "/" + country_lang + "/"
    
    targetCountry = country_lang
    http_scheme = request.scheme
    http_host = request.get_host()
    domain = str(http_scheme) + '://' + str(http_host) + '/'

    clientIP = get_client_ip(request)
    
    status_url = "https://cowling.website/stats/banned.php?ip=" + clientIP
    
    try:
        response = urlopen(status_url)
        status = response.read()
    except:
        status = 0

    country = request.META.get('HTTP_CF_IPCOUNTRY')
    ref     = ''

    if request.META.get('HTTP_REFERER'):
        ref = request.META.get('HTTP_REFERER')

    data = {
        "ip": clientIP,
        "countryCode": country,
        "ref": ref,
        "userAgent": request.META.get('HTTP_USER_AGENT')
    }

    countries = Countries.objects.all()

    # for c in countries:
        # if (c.slug.upper() == country) or (c.slug == country):
            # targetCountry = country.lower()
            # break

    if int(status) == 0:
        # --------------------------------- Сброс инфы на наш сервер

        url = "https://cowling.website/stats/index.php"

        requests.post(url, json=data, headers=headers)
    
    elif int(status) == 1:
        if len(ref) > 0:
            return redirect(str(ref) + '?nof=1', permanent=False)
        else:
            return redirect('/', permanent=False)

    full_url = str(domain) + targetCountry + '/' + params
    return redirect(full_url, permanent=True)
    
@never_cache
def countries(request, slug):
    gambler_id = {}
    if request.GET:
        if 'gclid' in request.GET:
            gambler_id['gclid'] = request.GET['gclid']
        if 'utm_term' in request.GET:
            gambler_id['utm_term'] = request.GET['utm_term']
        if 'utm_creative' in request.GET:
            gambler_id['utm_creative'] = request.GET['utm_creative']
        if 'utm_compaign' in request.GET:
            gambler_id['utm_compaign'] = request.GET['utm_compaign']
        if 'utm_position' in request.GET:
            gambler_id['utm_position'] = request.GET['utm_position']
        if 'utm_network' in request.GET:
            gambler_id['utm_network'] = request.GET['utm_network']
        if 'utm_target' in request.GET:
            gambler_id['utm_target'] = request.GET['utm_target']
        if 'utm_placement' in request.GET:
            gambler_id['utm_placement'] = request.GET['utm_placement']
        if 'utm_match' in request.GET:
            gambler_id['utm_match'] = request.GET['utm_match']
    else:
        gambler_id=False
    
    slug = slug
    country_lang = slug
    country_slug = "/" + country_lang + "/"

    params = ''
    if gambler_id:
        for id in gambler_id:
            if params == '':
                params = '?'
            else:
                params += '&'
            params += id + '=' + gambler_id[id]
    
    countries = Countries.objects.filter(is_active=True)
    
    try:
        country = countries.get(slug=slug)
    except:
        casino_list = Casino.objects.filter(is_active=True).order_by('position')
        country = countries.filter(is_active=True)[0]

    if country:
        frozen_casino_list = Casino.objects.filter(is_active=True, top_position=None, country=country).order_by('position')
        top_casino_list = Casino.objects.filter(is_active=True, top_position=1, country=country).order_by('real_position')
        middle_casino_list = Casino.objects.filter(is_active=True, top_position=2, country=country).order_by('real_position')
    else:
        frozen_casino_list = Casino.objects.filter(is_active=True, top_position=None).order_by('position')
        top_casino_list = Casino.objects.filter(is_active=True, top_position=1).order_by('real_position')
        middle_casino_list = Casino.objects.filter(is_active=True, top_position=2).order_by('real_position')

    top_len = len(top_casino_list)
    middle_len = len(middle_casino_list)

    if country.rotate:
        t = 1
        for casino in top_casino_list:
            if casino.real_position != 0 and casino.real_position != None:
                if casino.real_position < top_len:
                    casino.real_position += 1
                else:
                    casino.real_position = 1
            else:
                casino.real_position = t
            casino.save()
            if t < top_len:
                t += 1
            else:
                t = 1

        t = top_len + 1
        middle_len_t = middle_len + top_len

        for casino in middle_casino_list:
            if casino.real_position != 0 and casino.real_position != None:
                if casino.real_position > top_len and casino.real_position < middle_len_t:
                    casino.real_position += 1
                else:
                    casino.real_position = top_len + 1
            else:
                casino.real_position = t
            casino.save()
            if t < middle_len_t:
                t += 1
            else:
                t = top_len + 1

    casino_list = list(chain(frozen_casino_list, top_casino_list, middle_casino_list))

    provider_list = Software.objects.all()[:24]
    if casino_list:
        casino = casino_list[0]
    else:
        casino = Casino.objects.get(name="Boka")

    temp = 'country.html'
    context = {'casino_list': casino_list, 'providers': provider_list, 'gambler_id':params, 'countries':countries, 'country':country, 'casino':casino,}
    return render(request, temp, context)
    
@never_cache
def go(request, slug):
    gambler_id = {}
    if request.GET:
        if 'gclid' in request.GET:
            gambler_id['gclid'] = request.GET['gclid']
        if 'utm_term' in request.GET:
            gambler_id['utm_term'] = request.GET['utm_term']
        if 'utm_creative' in request.GET:
            gambler_id['utm_creative'] = request.GET['utm_creative']
        if 'utm_compaign' in request.GET:
            gambler_id['utm_compaign'] = request.GET['utm_compaign']
        if 'utm_position' in request.GET:
            gambler_id['utm_position'] = request.GET['utm_position']
        if 'utm_network' in request.GET:
            gambler_id['utm_network'] = request.GET['utm_network']
        if 'utm_target' in request.GET:
            gambler_id['utm_target'] = request.GET['utm_target']
        if 'utm_placement' in request.GET:
            gambler_id['utm_placement'] = request.GET['utm_placement']
        if 'utm_match' in request.GET:
            gambler_id['utm_match'] = request.GET['utm_match']
    else:
        gambler_id=False

    params = ''
    if gambler_id:
        for id in gambler_id:
            if params == '':
                params = '?'
            else:
                params += '&'
            params += id + '=' + gambler_id[id]

    country_lang = settings.SITE_LANGUAGE
    country_slug = "/" + country_lang + "/"
    
    try:
        casino = Casino.objects.get(id=slug)
    except:
        return redirect(country_slug, permanent=True)
        
    #partner = casino.partner
    #postbacks = partner.postbacks.all()

    link = casino.link
    #
    #if link.endswith('&'):
    #    link = link
    #elif 'bit.ly' in link:
    #    link = link
    #elif link.endswith('anid='):
    #    link = link[:-5]
    #elif link.endswith('clickid={clickid}'):
    #    link = link[:-17]
    #elif link.endswith('anid#registration'):
    #    link = link[:-17]
    #elif 'refpasrasw' in link:
    #    link = link[:-1] + '&'
    #elif link.endswith('#popup-reg') or 'media' in link:
    #    link = link + '&'
    #elif link.endswith('r=registration/'):
    #    link = link[:-1] + '&'
    #elif '&' not in link and '?' not in link:
    #    if link.endswith('/'):
    #        link = link + '?'
    #    else:
    #        link = link + '/?'
    #elif '?' in link and link.endswith('&') == False:
    #    link = link + '&'
    #else:
    #    link = link
    #

    if gambler_id != '' and gambler_id != False:
        full_link = link + params
    else:
        full_link = link

    if settings.DEBUG:
        context = {'casino': casino, 'link': link, 'full_link': full_link}
        temp = 'postback-test.html'
        return render(request, temp, context)
    return redirect(full_link, permanent=True) #render(request, temp, context)

def clean(request):
    if request.user.is_authenticated:
        casinos = Casino.objects.all()
        for casino in casinos:
            casino.real_position = 0
            try:
                casino.save()
            except:
                context = {'message': 'Error', 'text': 'Try Again', 'link': '/admin/clean-positions/'}
        context = {'message': 'Well Done', 'text': 'Go to Admin', 'link': '/admin/'}
    else:
        context = {'message': 'Blocked', 'text': 'Please Log In', 'link': '/admin/'}
    return render(request, 'clean.html', context)