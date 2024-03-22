# Generated by Django 5.0.3 on 2024-03-21 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulink',
            name='new_tab',
            field=models.BooleanField(default=False, verbose_name='Nova aba'),
        ),
        migrations.AlterField(
            model_name='menulink',
            name='text',
            field=models.CharField(max_length=50, verbose_name='Testo'),
        ),
        migrations.AlterField(
            model_name='menulink',
            name='url_or_path',
            field=models.CharField(max_length=2048, verbose_name='Url ou Caminho'),
        ),
    ]