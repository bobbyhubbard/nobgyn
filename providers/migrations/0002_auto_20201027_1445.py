# Generated by Django 3.1.2 on 2020-10-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='image_lrg',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='image_med',
            field=models.URLField(blank=True),
        ),
    ]