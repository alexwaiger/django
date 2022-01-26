from colorfield.fields import ColorField
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Theme(models.Model):
    name =  models.CharField(u'Название', max_length=50)
    bg_color = ColorField(u'Цвет фона #RRGGBB', max_length=7, blank=False, null=True, default='#000000')
    color = ColorField(u'Основной цвет #RRGGBB', max_length=7, blank=False, null=True, default='#FFFFFF')
    h_color = ColorField(u'Цвет хедера #RRGGBB', max_length=7, blank=False, null=True, default='#FFF000')
    bg_img = ThumbnailerImageField(u'Фоновое изображение (desktop 1280px)', upload_to="upload/img/custom/", blank=False, null=True)
    bg_tab_img = ThumbnailerImageField(u'Фоновое изображение (tablet 992px)', upload_to="upload/img/custom/", blank=True, null=True)
    bg_mob_img = ThumbnailerImageField(u'Фоновое изображение (mobile 480px)', upload_to="upload/img/custom/", blank=True, null=True)
    logo = ThumbnailerImageField(u'Логотип', upload_to="upload/img/site_logos/", blank=True, null=True)
    badge = ThumbnailerImageField(u'Значек (справа от лого)', upload_to="upload/img/site_badges/", blank=True, null=True)
    icons_color = models.BooleanField(u'Черно-белые иконки', default=False, blank=True, null=False)
    icon_to_top = models.BooleanField(u'Иконка GO TO TOP', default=False, blank=True, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Theme"
        verbose_name_plural  = u"Themes"