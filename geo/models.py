from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from decor.models import Theme

CURRENCY = (
    (None, None),
    ('€', '€'),
    ('$', '$'),
)

class Currency(models.Model):
    name =  models.CharField(u'name', max_length=50)
    acronym =  models.CharField(u'acronym', max_length=5, null=True, default=None)
    symbol =  models.CharField(u'symbol', max_length=5, blank=True, null=True, default=None)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/currency/", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Currency"
        verbose_name_plural  = u"Currencies"

class Countries(models.Model):
    is_active = models.BooleanField(u'Is Active', default=True, blank=False, null=False)
    name =  models.CharField(u'Название', max_length=50)
    image = ThumbnailerImageField(u'Flag', upload_to="upload/img/flags/", blank=False)
    currency = models.ForeignKey(Currency, related_name='country_currency', blank=True, null=True, default=None, on_delete=models.CASCADE)
    slug =  models.CharField(u'Обозначение (en)', max_length=2)
    header = models.CharField(u'Заголовок', max_length=100, blank=True, null=True)
    text = models.CharField(u'Текст', max_length=300, blank=True, null=True)
    promo1 = models.CharField(u'Текст в шапке (верх)', max_length=300, blank=True, null=True)
    promo2 = models.CharField(u'Текст в шапке (низ)', max_length=300, blank=True, null=True)
    theme = models.ForeignKey(Theme, related_name='country_theme', blank=True, null=True, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Country"
        verbose_name_plural  = u"Countries"
