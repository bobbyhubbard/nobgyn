# Generated by Django 3.1.2 on 2021-02-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='fax',
            field=models.CharField(default='(816) 781-7820', help_text='Fax display text', max_length=14),
        ),
    ]