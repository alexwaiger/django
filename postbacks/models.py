from django.db import models

class Postback(models.Model):
    is_active = models.BooleanField(u'Is Active', default=True, blank=False, null=False)
    name = models.CharField(u'name', max_length=50, blank=False, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Postback"
        verbose_name_plural  = u"Postbacks"
        
class Partner(models.Model):
    name = models.CharField(u'name', max_length=50, blank=False)
    postbacks = models.ManyToManyField(Postback, related_name='partner_program', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Partner"
        verbose_name_plural  = u"Partners"