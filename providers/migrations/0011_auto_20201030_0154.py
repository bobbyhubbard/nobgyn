# Generated by Django 3.1.2 on 2020-10-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0010_schoolrelationship_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='doctor',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='focus',
            field=models.CharField(default='Obstetrics & Gynecology', help_text='Ob, Gyn, or both?', max_length=50),
        ),
    ]