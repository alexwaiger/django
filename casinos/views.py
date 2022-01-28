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

from django.utils import translation

from .models import Casino, Software
from geo.models import Countries
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
    postbacks = Postback.objects.all()
    gambler_id = '000'
        
    if request.GET:
        for postback in postbacks:
            if postback.name in request.GET:
                gambler_id = request.GET[postback.name]
    else:
        gambler_id = False
        
    headers = {
        "Content-type": "application/json",
        "Accept": "text/plain",
        "Content-Encoding": "utf-8"
    }
    country_lang = settings.SITE_LANGUAGE
    country_slug = "/" + country_lang + "/"
    
    targetCountry = country_lang
    domain = request.build_absolute_uri()

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

    full_url = str(domain) + targetCountry + '/'
    return redirect(full_url, permanent=True)
    
@never_cache
def countries(request, slug):
    postbacks = Postback.objects.all()
    gambler_id = '000'
    
    slug = slug
    country_lang = slug
    country_slug = "/" + country_lang + "/"
        
    if request.GET:
        for postback in postbacks:
            if postback.name in request.GET:
                gambler_id = request.GET[postback.name]
    else:
        gambler_id = False
    
    countries = Countries.objects.filter(is_active=True)
    
    try:
        country = countries.get(slug=slug)
        casino_list = Casino.objects.filter(is_active=True, country=country).order_by('position')
    except:
        casino_list = Casino.objects.filter(is_active=True).order_by('position')
        country = countries.filter(is_active=True)[0]
        
    provider_list = Software.objects.all()[:24]
    if casino_list:
        casino = casino_list[0]
    else:
        casino = Casino.objects.get(name="Boka")
        
    if country_lang == 'en':
        temp = 'country.html'
    else:
        temp = country_lang + '.html'
        
    context = {'casino_list': casino_list, 'providers': provider_list, 'gambler_id':gambler_id, 'countries':countries, 'country':country, 'casino':casino,}
    return render(request, temp, context)
    
@never_cache
def go(request, slug):
    country_lang = settings.SITE_LANGUAGE
    country_slug = "/" + country_lang + "/"
    
    try:
        casino = Casino.objects.get(id=slug)
    except:
        return redirect(country_slug, permanent=True)
        
    partner = casino.partner
    postbacks = partner.postbacks.all()
    
    postback_params = ''
    gambler_id = '000'
        
    if request.GET:
        if 'id' in request.GET:
            gambler_id = request.GET['id']
    else:
        gambler_id = False
    
    iter = 0
    if gambler_id != False and gambler_id != '000':
        for postback in postbacks:
            if iter == 0:
                postback_params = postback.name + '=' + gambler_id
            else:
                postback_params = postback_params + '&' + postback.name + '=' + gambler_id
            iter += 1
    
    if casino.link:
        link = casino.link
    else:
        link = country_slug
    
    if link.endswith('&'):
        link = link
    elif 'bit.ly' in link:
        link = link
    elif link.endswith('anid='):
        link = link[:-5]
    elif link.endswith('clickid={clickid}'):
        link = link[:-17]    
    elif link.endswith('anid#registration'):
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
    elif '?' in link and link.endswith('anid#registration') == False:
        link = link + '&'       
    else:
        link = link
    
    if gambler_id:
        full_link = link + postback_params
    else:
        full_link = link

    if settings.DEBUG:
        context = {'casino': casino, 'partner': partner, 'postbacks':postbacks, 'link': link, 'full_link': full_link}
        temp = 'postback-test.html'
        return render(request, temp, context)
    return redirect(full_link, permanent=True) #render(request, temp, context)