# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from postbacks.models import Partner
from geo.models import Countries

LICENSES = (
    ('1', 'Curacao'),
    ('2', 'Malta'),
    ('3', 'AAMS'),
)

TOPS = (
    ('1', 'First'),
    ('2', 'Second'),
)

COLORS = (
    ('blue-band.png', 'Blue'),
    ('darkblue-band.png', 'DarkBlue'),
    ('red-band.png', 'Red'),
    ('green-band.png', 'Green'),
    ('yellow-band.png', 'Yellow'),
    ('violet-band.png', 'Violet'),
    ('purple-band.png', 'Purple'),
    ('orange-band.png', 'Orange'),
)


class Payment(models.Model):
    name =  models.CharField(u'name', max_length=50, blank=False)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/pay/", blank=False, null=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Payment"
        verbose_name_plural  = u"Payments"
        
class Software(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/soft/", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Software"
        verbose_name_plural  = u"Softwares"
        
class Badge(models.Model):
    name =  models.CharField(u'Name', max_length=20)
    color = models.CharField(u'Color', max_length=50, choices = COLORS, blank=True, null=True)
    text =  models.CharField(u'Text', max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Badge"
        verbose_name_plural  = u"Badges"

class Casino(models.Model):
    is_active = models.BooleanField(u'Is Active', default=False, blank=False, null=False)
    name = models.CharField(u'Title', max_length=50)
    partner = models.ForeignKey(Partner, related_name='aff', blank=True, null=True, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, related_name='casino_badge', blank=True, null=True, on_delete=models.CASCADE)
    license = models.CharField(u'License', max_length=3, choices = LICENSES, default=2)
    logo = ThumbnailerImageField(u'Casino Logo', upload_to="upload/img/logos/")
    country = models.ManyToManyField(Countries, default=None, related_name='countries', blank=True)
    
    pay = models.ManyToManyField(Payment, related_name='pays', blank=True)
    position = models.IntegerField(u'Position', default=0, blank=False, null=False)
    top_position = models.CharField(u'Top position', max_length=3, choices=TOPS, default=2, blank=True, null=True)
    link = models.CharField(u'Link', max_length=180, blank=False, null=True, default=None)
    adv1 = models.CharField(u'Promo1', max_length=50, blank=True, null=True)
    adv2 = models.CharField(u'Promo2', max_length=50, blank=True, null=True)
    adv3 = models.CharField(u'Promo3', max_length=50, blank=True, null=True)
    
    min_dep = models.IntegerField(u'Min deposit', blank=False, null=False, default=0)
    bonus = models.IntegerField(u'Welcome bonus', blank=False, null=False, default=0)
    limit = models.IntegerField(u'Bonus limit', null=False, blank=False, default=0)
    cashback = models.IntegerField(u'CashBack %', null=False, blank=False, default=0)
    fs = models.IntegerField(u'Free Spins', null=False, blank=False, default=0)

    real_position = models.IntegerField(u'Real Position', default=None, blank=True, null=True)
    click = models.IntegerField(u'Clicks', default=0, blank=True, null=True)

    def __str__(self):
        return self.name
        
    def bonus_limit(self):
        limit = self.limit
        short_limit = ''
        if limit >= 1000:
            if limit < 10000:
                limit = str(limit)
                short_limit = limit[0] + '.' + limit[1] + 'K'
            else:
                limit = str(limit)
                short_limit = limit[:-3] + 'K'
        else:
            limit = str(limit)
            short_limit = limit
        return short_limit

    class Meta:
        verbose_name  = u"Casino"
        verbose_name_plural  = u"Casinos"