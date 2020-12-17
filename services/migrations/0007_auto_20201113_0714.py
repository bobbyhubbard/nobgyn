# Generated by Django 3.1.2 on 2020-11-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20201109_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='title',
        ),
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(default='', help_text='Service name', max_length=50),
        ),
    ]
