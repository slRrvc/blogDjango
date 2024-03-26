from django.db import models
from utils.model_validators import velidate_png

class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    text = models.CharField(max_length=50, verbose_name='Testo do link')
    url_or_path = models.CharField(max_length=2048, verbose_name='Url ou Caminho')
    new_tab = models.BooleanField(default=False, verbose_name='Abrir em nova aba')
    site_setup = models.ForeignKey(
        'SiteSetup', 
        on_delete = models.CASCADE,
        blank= True,
        null = True,
        default = None,
        verbose_name= 'Site'
    )

    def __str__(self):
        return self.text
    
class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Site'

    title = models.CharField(max_length=65, verbose_name = 'Titulo do Site')
    description = models.CharField(max_length=255, verbose_name = 'Descrição')
    show_header = models.BooleanField(default=True, verbose_name = 'Mostrar cabeçalho')
    show_search = models.BooleanField(default=True, verbose_name = 'Mostrar pesquisa')
    show_menu = models.BooleanField(default=True, verbose_name = 'Mostrar menu')
    show_description = models.BooleanField(default=True, verbose_name = 'Mostrar descrição')
    show_pagination = models.BooleanField(default=True, verbose_name = 'Mostrar paginação')
    show_footer = models.BooleanField(default=True, verbose_name = 'Mostrar rodapé')

    favicon =models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True,
        default='',
        validators=[velidate_png],
    )
 
    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title