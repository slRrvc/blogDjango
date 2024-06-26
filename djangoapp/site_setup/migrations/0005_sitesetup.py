# Generated by Django 5.0.3 on 2024-03-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_alter_menulink_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, verbose_name='Titulo do Site')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('show_header', models.BooleanField(default=True, verbose_name='Mostrar cabeçalho')),
                ('show_search', models.BooleanField(default=True, verbose_name='Mostrar pesquisa')),
                ('show_menu', models.BooleanField(default=True, verbose_name='Mostrar menu')),
                ('show_description', models.BooleanField(default=True, verbose_name='Mostrar descrição')),
                ('show_pagination', models.BooleanField(default=True, verbose_name='Mostrar paginação')),
                ('show_footer', models.BooleanField(default=True, verbose_name='Mostrar rodapé')),
            ],
            options={
                'verbose_name': 'Configurações do site',
                'verbose_name_plural': 'Configurações dos sites',
            },
        ),
    ]
