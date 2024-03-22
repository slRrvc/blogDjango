from django.db import models


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50, verbose_name='Testo do link')
    url_or_path = models.CharField(max_length=2048, verbose_name='Url ou Caminho')
    new_tab = models.BooleanField(default=False, verbose_name='Abrir em nova aba')

    def __str__(self):
        return self.text