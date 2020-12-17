# Generated by Django 3.1.2 on 2020-11-12 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='', help_text='What should this banner message say?')),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now, help_text='When should this banner message be published?')),
                ('expiration_date', models.DateTimeField(blank=True, help_text='Should this banner stop being displayed on a specific date? (Optional)', null=True)),
            ],
        ),
    ]
