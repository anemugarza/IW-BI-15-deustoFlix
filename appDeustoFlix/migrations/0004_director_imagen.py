# Generated by Django 4.2.6 on 2023-11-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustoFlix', '0003_pelicula_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
    ]
